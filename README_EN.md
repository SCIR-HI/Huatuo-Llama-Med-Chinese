[**中文**](./README.md) | [**English**](./README_EN.md)
<p align="center" width="100%">
<a href="https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/" target="_blank"><img src="assets/logo/logo.png" alt="SCIR-HI-HuaTuo" style="width: 60%; min-width: 300px; display: block; margin: auto;"></a>
</p>
# BenTsao (original name: HuaTuo): Tuning LLaMA Model With Chinese Medical Instructions

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/blob/main/LICENSE) [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

This repo open-sources the Instruct-tuned LLaMA-7B model that has been fine-tuned with Chinese medical instructions. We constructed a Chinese medical instruct-tuning dataset using medical knowledge graphs and the GPT3.5 API, and performed instruction-tuning on LLaMA based on this dataset, improving its question-answering performance in the medical field.

In addition, we tried to use the GPT3.5 API to integrate [conclusions] in the medical literature as external information into multiple rounds of dialogue, and based on this, we fine-tuned LLaMA. At present, we only open model parameters trained for the single disease "liver cancer". In the future, we plan to release a medical dialogue dataset incorporating medical literature conclusions, and plan to train models for 16 diseases related to "liver, gallbladder and pancreas".

We also trained a medical version of ChatGLM: [ChatGLM-6B-Med](https://github.com/SCIR-HI/Med-ChatGLM) based on the same data.

We are about to release our new model [扁鹊（PienChueh）](https://github.com/SCIR-HI/Bian-Que_Pien-Chueh). 


## A Quick Start
Firstly, install the required packages. It is recommended to use Python 3.9 or above

```
pip install -r requirements.txt
```
### Model download
LORA weights can be downloaded through Baidu Netdisk or Huggingface.

-Based on medical knowledge base. [Baidu Netdisk](https://pan.baidu.com/s/1jih-pEr6jzEa6n2u6sUMOg?pwd=jjpf) or [HuggingFace](https://huggingface.co/thinksoso/lora-llama-med).
-Based on medical literature. [Baidu Netdisk](https://pan.baidu.com/s/1jADypClR2bLyXItuFfSjPA?pwd=odsk)

Download the LORA weight file and extract it. The format of the extracted file should be as follows:

```
#Based on medical knowledge base
lora-llama-med/
  - adapter_config.json		# LoRA weight configuration file
  - adapter_model.bin		# LoRA weights

#Based on medical literature
lora-llama-med-literature/
  - adapter_config.json   # LoRA weight configuration file
  - adapter_model.bin   # LoRA weights

```

### Infer
We provided some test cases in `./data/infer.json`, which can be replaced with other datasets. Please make sure to keep the format consistent.

Run the infer script

```
#Based on medical knowledge base
bash ./scripts/infer.sh

#Based on medical literature
#single-epoch
bash ./scripts/infer-literature-single.sh

#multi-epoch
bash ./scripts/infer-literature-multi.sh
```

### Dataset construction
We used both publicly available and self-built Chinese medical knowledge bases, with a primary reference to [cMeKG](https://github.com/king-yyf/CMeKG_tools). The medical knowledge base is built around diseases, drugs, and diagnostic indicators, with fields including complications, risk factors, histological examinations, clinical symptoms, drug treatments, and adjuvant therapies. An example of the knowledge base is shown below:


```
{"中心词": "偏头痛", "相关疾病": ["妊娠合并偏头痛", "恶寒发热"], "相关症状": ["皮肤变硬", "头部及眼后部疼痛并能听到连续不断的隆隆声", "晨起头痛加重"], "所属科室": ["中西医结合科", "内科"], "发病部位": ["头部"]}
```
We used the GPT3.5 API to build a Question-Answer dataset around a medical knowledge base, with multiple prompts to fully leverage the knowledge.

An example of the training dataset for instruct-tuning is shown below:


```
"问题：一位年轻男性长期使用可卡因，突然出现胸痛、呕吐、出汗等症状，经检查发现心电图反映心肌急性损伤，请问可能患的是什么疾病？治疗方式是什么？"
回答: 可能患的是心肌梗塞，需要进行维拉帕米、依普利酮、硝酸甘油、ß阻滞剂、吗啡等药物治疗，并进行溶栓治疗、低分子量肝素、钙通道阻滞剂等辅助治疗。此外需要及时停用可卡因等药物，以防止病情加重。"
```

We provided a training dataset for the model, consisting of more than eight thousand entries. It should be noted that although knowledge has been incorporated into the construction of the training set, there are still errors and imperfections. We will use better strategies to iteratively update the dataset in the future.

The quality of the dataset for instruct-tuning is still limited. We will continue to iterate and improve it. Meanwhile, the medical knowledge base and dataset construction code are still being organized and will be released once completed.

In addition, we collected Chinese medical literature on liver cancer in 2023, and used the GPT3.5 interface to collect multiple rounds of question-and-answer data around the medical literature. We provide 1k training examples in `./data_literature/liver_cancer.json`. At present, the quality of training samples is still limited. In the future, we will further iterate the data and release it in the form of `public dataset`. An example of a training sample is as follows:

<p align="center" width="100%">

<a href="https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/" target="_blank"><img src="assets/case.png" alt="SCIR-HI-HuaTuo-literature" style="width: 100%; min-width: 300px; display: block; margin: auto;"></a>

</p>


### Finetune
To fine-tune LLaMA with your own dataset, please construct your dataset following the format of `./data/llama_data.json` and run the finetune script.

```
bash ./scripts/finetune.sh
```



## Training details
### GPU resource
We trained the model on an A100-SXM-80GB for a total of 10 epochs, which took approximately 2 hours and 17 minutes. With a batch size of 128, the GPU memory usage was around 40GB. We expect that GPU with 24GB or more of memory, such as the 3090/4090, will be able to support the model well, and the batch size can be adjusted based on the size of the GPU memory.


### Experiments
Parameter settings and details training process can be found in the wandb log:
https://wandb.ai/thinksoso/llama_med/runs/a5wgcnzt/overview?workspace=user-thinksoso

## Comparison of models

| Input入 | Llama output  | Alpaca output | HuaTuo output |
|:------------- |:---------------| :-------------|:-------------|
|小张最近感觉身体不适，出现心悸、气促等症状。体检发现心脏扩大、搏动减弱。|问题：小张最近感觉身体不适，出现心悸、气促等症状。体检发现心脏扩大、搏动减弱。| 最近，小张一直感觉身体不舒服，有心烦意乱、呼吸急促等症状。体格检查显示心脏增大，肌肉无力。|**小张可能患有心肌炎，建议尽快到医院进行检查和治疗。治疗方案包括药物治疗和手术治疗。**|
|麻风病和儿童哮喘的病因是否一致？|儿童哮喘和麻风病的病因是一致，但是儿童哮喘和麻风病的病因不一致|是的，哮喘和儿童喘息有相似的原因。| **不一致，麻风病的病因是麻风杆菌感染，而儿童哮喘的病因是喂养不良、吸烟等因素。**|
|一位患者出现了持续性的胀痛和黄疸，经影像学检查后确诊为肝胆管结石病，应该采取哪些治疗方案？|肝胆管结石病患者应该采取哪些治疗方案？|患者应接受手术和化疗相结合的治疗。| **针对肝胆管结石病，治疗方案包括手术治疗、药物治疗和辅助治疗等。具体治疗方案需要根据患者的具体情况而定。**|

## Contributors

This project was founded by the Health Intelligence Group of the Research Center for Social Computing and Information Retrieval at Harbin Institute of Technology, including [Haochun Wang](https://github.com/s65b40), [Yanrui Du](https://github.com/DYR1), [Chi Liu](https://github.com/thinksoso), [Rui Bai](https://github.com/RuiBai1999), [Nuwa Xi](https://github.com/rootnx), [Yuhan Chen](https://github.com/Imsovegetable), [Zewen Qiang](https://github.com/1278882181), [Jianyu Chen](https://github.com/JianyuChen01), [Zijian Li](https://github.com/FlowolfzzZ) supervised by Associate Professor Sendong Zhao, Professor Bing Qin, and Professor Ting Liu.


## Acknowledgements

This project has referred the following open-source projects. We would like to express our gratitude to the developers and researchers involved in those projects.

- Facebook LLaMA: https://github.com/facebookresearch/llama
- Stanford Alpaca: https://github.com/tatsu-lab/stanford_alpaca
- alpaca-lora by @tloen: https://github.com/tloen/alpaca-lora
- CMeKG https://github.com/king-yyf/CMeKG_tools
- 文心一言 https://yiyan.baidu.com/welcome The logo of this project is automatically generated by Wenxin Yiyan.

## Disclaimer
The resources related to this project are for academic research purposes only and strictly prohibited for commercial use. When using portions of third-party code, please strictly comply with the corresponding open source licenses. The content generated by the model is influenced by factors such as model computation, randomness, and quantization accuracy loss, and this project cannot guarantee its accuracy. The vast majority of the dataset used in this project is generated by the model, and even if it conforms to certain medical facts, it cannot be used as the basis for actual medical diagnosis. This project does not assume any legal liability for the content output by the model, nor is it responsible for any losses that may be incurred as a result of using the related resources and output results.


## Citation
If you use the data or code from this project, please declare the reference:

```
@misc{wang2023huatuo,
      title={HuaTuo: Tuning LLaMA Model with Chinese Medical Knowledge}, 
      author={Haochun Wang and Chi Liu and Nuwa Xi and Zewen Qiang and Sendong Zhao and Bing Qin and Ting Liu},
      year={2023},
      eprint={2304.06975},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```