import sys
import json

import fire
import gradio as gr
import torch
import transformers
from peft import PeftModel
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer

from utils.prompter import Prompter

if torch.cuda.is_available():
    device = "cuda"

def load_instruction(instruct_dir):
    input_data = []
    with open(instruct_dir, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            d = json.loads(line)
            input_data.append(d)
    return input_data


def main(
    load_8bit: bool = False,
    base_model: str = "",
    # the infer data, if not exists, infer the default instructions in code
    single_or_multi: str = "",
    use_lora: bool = True,
    lora_weights: str = "tloen/alpaca-lora-7b",
    # The prompt template to use, will default to med_template.
    prompt_template: str = "med_template",
):
    prompter = Prompter(prompt_template)
    tokenizer = LlamaTokenizer.from_pretrained(base_model)
    model = LlamaForCausalLM.from_pretrained(
        base_model,
        load_in_8bit=load_8bit,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    if use_lora:
        print(f"using lora {lora_weights}")
        model = PeftModel.from_pretrained(
            model,
            lora_weights,
            torch_dtype=torch.float16,
        )
    # unwind broken decapoda-research config
    model.config.pad_token_id = tokenizer.pad_token_id = 0  # unk
    model.config.bos_token_id = 1
    model.config.eos_token_id = 2
    if not load_8bit:
        model.half()  # seems to fix bugs for some users.

    model.eval()

    if torch.__version__ >= "2" and sys.platform != "win32":
        model = torch.compile(model)

    def evaluate(
        instruction,
        input=None,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        max_new_tokens=256,
        **kwargs,
    ):
        prompt = prompter.generate_prompt(instruction, input)
        inputs = tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"].to(device)
        generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            num_beams=num_beams,
            **kwargs,
        )
        with torch.no_grad():
            generation_output = model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                max_new_tokens=max_new_tokens,
            )
        s = generation_output.sequences[0]
        output = tokenizer.decode(s)
        return prompter.get_response(output)

    if single_or_multi == "multi":

        response=""
        instruction=""
        for _ in range(0,5):  
            inp=input("请输入:")
            inp="<user>: " + inp
            instruction=instruction+inp
            response=evaluate(instruction)
            response=response.replace('\n','')
            print("Response:", response)
            instruction= instruction + " <bot>: " + response


    elif single_or_multi == "single":
        for instruction in [
            "肝癌是什么？有哪些症状和迹象？",
            "肝癌是如何诊断的？有哪些检查和测试可以帮助诊断？",
            "Sorafenib是一种口服的多靶点酪氨酸激酶抑制剂，它的作用机制是什么？",
            "Regorafenib是一种口服的多靶点酪氨酸激酶抑制剂，它的作用机制是什么？它和Sorafenib有什么不同？",
            "肝癌药物治疗的副作用有哪些？如何缓解这些副作用？",
            "肝癌药物治疗的费用高昂，如何降低治疗的经济负担？",
            "我想了解一下β-谷甾醇是否可作为肝癌的治疗药物",
            "能介绍一下最近Hsa＿circ＿0008583在肝细胞癌治疗中的潜在应用的研究么?"
        ]:  
            print("instruction:",instruction)
            instruction="<user>: "+instruction
            print("Response:", evaluate(instruction))
          


if __name__ == "__main__":
    fire.Fire(main)
