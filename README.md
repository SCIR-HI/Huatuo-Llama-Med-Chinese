[**中文**](./README.md) | [**English**](./README_EN.md)

<p align="center" width="100%">
<a href="https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/" target="_blank"><img src="assets/logo/logo_new.png" alt="SCIR-HI-HuaTuo" style="width: 60%; min-width: 300px; display: block; margin: auto;"></a>
</p>

  

# 本草[原名：华驼(HuaTuo)]: 基于中文医学知识的大语言模型指令微调

### BenTsao (original name: HuaTuo): Instruction-tuning Large Language Models With Chinese Medical Knowledge

[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/blob/main/LICENSE) [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

  
本项目开源了经过中文医学指令精调/指令微调(Instruction-tuning) 的大语言模型集，包括LLaMA、Alpaca-Chinese、Bloom、活字模型等。


我们基于医学知识图谱以及医学文献，结合ChatGPT API构建了中文医学指令微调数据集，并以此对各种基模型进行了指令微调，提高了基模型在医疗领域的问答效果。


## News

**[2024/07/25][《基于知识微调的大语言模型可靠中文医学回复生成方法》](https://dl.acm.org/doi/abs/10.1145/3686807)被ACM TKDD录用**

**[2023/09/24]发布[《面向智慧医疗的大语言模型微调技术》](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/tree/main/doc/Tuning_Methods_for_LLMs_towards_Health_Intelligence.pdf)**


<details>
<summary>历史新闻</summary>

**[2023/09/12]在arxiv发布[《探索大模型从医学文献中交互式知识的获取》](https://arxiv.org/pdf/2309.04198.pdf)**

**[2023/09/08]在arxiv发布[《基于知识微调的大语言模型可靠中文医学回复生成方法》](https://arxiv.org/pdf/2309.04175.pdf)**  

**[2023/08/07] 🔥🔥增加了基于[活字](https://github.com/HIT-SCIR/huozi)进行指令微调的模型发布，模型效果显著提升。🔥🔥**

[2023/08/05] 本草模型在CCL 2023 Demo Track进行Poster展示。

 [2023/08/03] SCIR实验室开源[活字](https://github.com/HIT-SCIR/huozi)通用问答模型，欢迎大家关注🎉🎉

[2023/07/19] 增加了基于[Bloom](https://huggingface.co/bigscience/bloom-7b1)进行指令微调的模型发布。

[2023/05/12] 模型由"华驼"更名为"本草"。

[2023/04/28] 增加了基于[中文Alpaca大模型](https://github.com/ymcui/Chinese-LLaMA-Alpaca)进行指令微调的模型发布。

[2023/04/24] 增加了基于LLaMA和医学文献进行指令微调的模型发布。

</details>



[2023/03/31] 增加了基于LLaMA和医学知识库进行指令微调的模型发布。


## A Quick Start

首先安装依赖包，python环境建议3.9+

```
pip install -r requirements.txt

```

针对所有基模型，我们采用了半精度基模型LoRA微调的方式进行指令微调训练，以在计算资源与模型性能之间进行权衡。

### 基模型
 - [活字1.0](https://github.com/HIT-SCIR/huozi)，哈尔滨工业大学基于Bloom-7B二次开发的中文通用问答模型
 - [Bloom-7B](https://huggingface.co/bigscience/bloomz-7b1)
 - [Alpaca-Chinese-7B](https://github.com/ymcui/Chinese-LLaMA-Alpaca)，基于LLaMA二次开发的中文问答模型
 - [LLaMA-7B](https://huggingface.co/decapoda-research/llama-7b-hf)
 
### LoRA模型权重下载

LoRA权重可以通过百度网盘或Hugging Face下载：

1. 🔥对活字进行指令微调的LoRA权重文件
  - 基于医学知识库以及医学问答数据集 [百度网盘](https://pan.baidu.com/s/1BPnDNb1wQZTWy_Be6MfcnA?pwd=m21s)
2. 对Bloom进行指令微调的LoRA权重文件
 - 基于医学知识库以及医学问答数据集 [百度网盘](https://pan.baidu.com/s/1jPcuEOhesFGYpzJ7U52Fag?pwd=scir)和[Hugging Face](https://huggingface.co/lovepon/lora-bloom-med-bloom)
3. 对Alpaca进行指令微调的LoRA权重文件
 - 基于医学知识库 [百度网盘](https://pan.baidu.com/s/16oxcjzXnXjDpL8SKihgNxw?pwd=scir)和[Hugging Face](https://huggingface.co/lovepon/lora-alpaca-med)
 - 基于医学知识库和医学文献 [百度网盘](https://pan.baidu.com/s/1HDdK84ASHmzOFlkmypBIJw?pwd=scir)和[Hugging Face](https://huggingface.co/lovepon/lora-alpaca-med-alldata)
4. 对LLaMA进行指令微调的LoRA权重文件
 - 基于医学知识库 [百度网盘](https://pan.baidu.com/s/1jih-pEr6jzEa6n2u6sUMOg?pwd=jjpf)和[Hugging Face](https://huggingface.co/thinksoso/lora-llama-med)
 - 基于医学文献 [百度网盘](https://pan.baidu.com/s/1jADypClR2bLyXItuFfSjPA?pwd=odsk)和[Hugging Face](https://huggingface.co/lovepon/lora-llama-literature)



下载LoRA权重并解压，解压后的格式如下：


```
**lora-folder-name**/
  - adapter_config.json   # LoRA权重配置文件
  - adapter_model.bin   # LoRA权重文件
```

基于相同的数据，我们还训练了医疗版本的ChatGLM模型: [ChatGLM-6B-Med](https://github.com/SCIR-HI/Med-ChatGLM)


### Infer

我们在`./data/infer.json`中提供了一些测试用例，可以替换成其它的数据集，请注意保持格式一致
  

运行infer脚本


```
#基于医学知识库
bash ./scripts/infer.sh

#基于医学文献
#单轮
bash ./scripts/infer-literature-single.sh

#多轮
bash ./scripts/infer-literature-multi.sh
```

infer.sh脚本代码如下，请将下列代码中基模型base_model、lora权重lora_weights以及测试数据集路径instruct_dir进行替换后运行

    python infer.py \
		    --base_model 'BASE_MODEL_PATH' \
		    --lora_weights 'LORA_WEIGHTS_PATH' \
		    --use_lora True \
		    --instruct_dir 'INFER_DATA_PATH' \
		    --prompt_template 'TEMPLATE_PATH'
 

**_提示模板的选择与模型相关，详情如下：_**

| 活字&Bloom                      | LLaMA&Alpaca                                                                          |                                       
|:------------------------------|:--------------------------------------------------------------------------------------|
| `templates/bloom_deploy.json` | 基于医学知识库`templates/med_template.json` <br>  基于医学文献`templates/literature_template.json` |



也可参考`./scripts/test.sh`

  

## 方法

基模型在医学问答场景下效果有限，指令微调是一种高效的使基模型拥有回答人类问题能力的方法。



### 数据集构建
#### 医学知识库
我们采用了公开和自建的中文医学知识库，主要参考了[cMeKG](https://github.com/king-yyf/CMeKG_tools)。

医学知识库围绕疾病、药物、检查指标等构建，字段包括并发症，高危因素，组织学检查，临床症状，药物治疗，辅助治疗等。知识库示例如下:


```

{"中心词": "偏头痛", "相关疾病": ["妊娠合并偏头痛", "恶寒发热"], "相关症状": ["皮肤变硬", "头部及眼后部疼痛并能听到连续不断的隆隆声", "晨起头痛加重"], "所属科室": ["中西医结合科", "内科"], "发病部位": ["头部"]}

```

我们利用GPT3.5接口围绕医学知识库构建问答数据，设置了多种Prompt形式来充分利用知识。

指令微调的训练集数据示例如下：

```

"问题：一位年轻男性长期使用可卡因，突然出现胸痛、呕吐、出汗等症状，经检查发现心电图反映心肌急性损伤，请问可能患的是什么疾病？治疗方式是什么？"

回答: 可能患的是心肌梗塞，需要进行维拉帕米、依普利酮、硝酸甘油、ß阻滞剂、吗啡等药物治疗，并进行溶栓治疗、低分子量肝素、钙通道阻滞剂等辅助治疗。此外需要及时停用可卡因等药物，以防止病情加重。"

```

  

我们提供了模型的训练数据集，共计八千余条，需要注意的是，虽然训练集的构建融入了知识，但是仍存在错误和不完善的地方，后续我们会利用更好的策略迭代更新数据集。

指令微调数据集质量仍有限，后续将进行不断迭代，同时医学知识库和数据集构建代码还在整理中，整理完成将会发布。

#### 医学文献

此外，我们收集了2023年关于肝癌疾病的中文医学文献，利用GPT3.5接口围绕医学文献的【结论】构建多轮问答数据。在·`./data_literature/liver_cancer.json`中我们提供了其中的1k条训练样例。目前，训练样本的质量仍然有限，在后续我们会进一步迭代数据，会以`公开数据集`的形式对外进行发布。训练样本的示例如下：

<p align="center" width="100%">

<a href="https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/" target="_blank"><img src="assets/case.png" alt="SCIR-HI-HuaTuo-literature" style="width: 100%; min-width: 300px; display: block; margin: auto;"></a>

</p>

目前，我们只开放针对"肝癌"单个疾病训练的模型参数。在未来，我们计划发布融入文献结论的医学对话数据集，并且会针对“肝胆胰”相关16种疾病训练模型。

相关细节可参考我们的文章：[《探索大模型从医学文献中交互式知识的获取》](https://arxiv.org/pdf/2309.04198.pdf)
  

### Finetune

如果想用自己的数据集微调大语言模型，请按照`./data/llama_data.json`中的格式构建自己的数据集

运行finetune脚本

```

bash ./scripts/finetune.sh

```

  
  
  

## 训练细节

### 计算资源需求参考

基于LLaMA模型的指令微调过程中，我们在一张A100-SXM-80GB显卡上进行了训练，训练总轮次10轮，耗时约2h17m。batch_size=128的情况下显存占用在40G左右。预计3090/4090显卡(24GB显存)以上显卡可以较好支持，根据显存大小来调整batch_size。


### 实验过程

超参设置和实验过程可以参考wandb的链接:

https://wandb.ai/thinksoso/llama_med/runs/a5wgcnzt/overview?workspace=user-thinksoso

  

## 模型效果对比

注：测试于2023年3月
  
| 测试输入 | Llama输出  | Alpaca输出 | BenTsao本草输出                                             |
|:------------- |:---------------| :-------------|:--------------------------------------------------------|
|小张最近感觉身体不适，出现心悸、气促等症状。体检发现心脏扩大、搏动减弱。|问题：小张最近感觉身体不适，出现心悸、气促等症状。体检发现心脏扩大、搏动减弱。| 最近，小张一直感觉身体不舒服，有心烦意乱、呼吸急促等症状。体格检查显示心脏增大，肌肉无力。| **小张可能患有心肌炎，建议尽快到医院进行检查和治疗。治疗方案包括药物治疗和手术治疗。**           |
|麻风病和儿童哮喘的病因是否一致？|儿童哮喘和麻风病的病因是一致，但是儿童哮喘和麻风病的病因不一致|是的，哮喘和儿童喘息有相似的原因。| **不一致，麻风病的病因是麻风杆菌感染，而儿童哮喘的病因是喂养不良、吸烟等因素。**              |
|一位患者出现了持续性的胀痛和黄疸，经影像学检查后确诊为肝胆管结石病，应该采取哪些治疗方案？|肝胆管结石病患者应该采取哪些治疗方案？|患者应接受手术和化疗相结合的治疗。| **针对肝胆管结石病，治疗方案包括手术治疗、药物治疗和辅助治疗等。具体治疗方案需要根据患者的具体情况而定。** |





   
## 常见问题
1. Q: 为什么更名为"本草"？
   
   A: 为SCIR实验室大语言模型命名一致性，中文医学大模型名称调整为"本草"。

2. Q: 为什么是"华驼"而不是"华佗"？ 
   
   A: 叫”驼“是因为我们的基模型LLaMA是美洲驼，Alpaca是羊驼，受他们名字的启发以及华佗的谐音梗，我们将我们的模型起名为华驼。

3. Q: 有使用中医理论或者中医数据吗？
    
   A: 目前还没有
   
4. Q: 模型运行的结果不同、效果有限
   
   A: 由于生成模型生成多样性的考量，多次运行的结果可能会有差异。当前开源的模型由于LLaMA及Alpaca中文语料有限，且知识结合的方式较为粗糙，请大家尝试bloom-based和活字-based的模型。
   
5. Q: 模型无法运行/推理内容完全无法接受
   
   A: 请确定已安装requirements中的依赖、配置好cuda环境并添加环境变量、正确输入下载好的模型以及lora的存储位置；推理内容如存在重复生成或部分错误内容属于llama-based模型的偶发现象，与llama模型的中文能力、训练数据规模以及超参设置均有一定的关系，请尝试基于活字的新模型。如存在严重问题，请将运行的文件名、模型名、lora等配置信息详细描述在issue中，谢谢大家。
   
6.	Q: 发布的若干模型哪个最好？

    A: 根据我们的经验，基于活字模型的效果相对更好一些。 
 



## 项目参与者

本项目由哈尔滨工业大学社会计算与信息检索研究中心健康智能组[王昊淳](https://haochun.wang) 、[杜晏睿](https://github.com/DYR1)、[刘驰](https://github.com/thinksoso)、[白睿](https://github.com/RuiBai1999)、[席奴瓦](https://github.com/rootnx)、[陈雨晗](https://github.com/Imsovegetable)、[强泽文](https://github.com/1278882181)、[陈健宇](https://github.com/JianyuChen01)、[李子健](https://github.com/FlowolfzzZ)完成，指导教师为[赵森栋](http://homepage.hit.edu.cn/stanzhao?lang=zh)副教授，秦兵教授以及刘挺教授。

  

## 致谢

  

本项目参考了以下开源项目，在此对相关项目和研究开发人员表示感谢。

- 活字: https://github.com/HIT-SCIR/huozi
- Facebook LLaMA: https://github.com/facebookresearch/llama
- Stanford Alpaca: https://github.com/tatsu-lab/stanford_alpaca
- alpaca-lora by @tloen: https://github.com/tloen/alpaca-lora
- CMeKG https://github.com/king-yyf/CMeKG_tools
- 文心一言 https://yiyan.baidu.com/welcome 本项目的logo由文心一言自动生成

  

## 免责声明

本项目相关资源仅供学术研究之用，严禁用于商业用途。使用涉及第三方代码的部分时，请严格遵循相应的开源协议。模型生成的内容受模型计算、随机性和量化精度损失等因素影响，本项目无法对其准确性作出保证。本项目数据集绝大部分由模型生成，即使符合某些医学事实，也不能被用作实际医学诊断的依据。对于模型输出的任何内容，本项目不承担任何法律责任，亦不对因使用相关资源和输出结果而可能产生的任何损失承担责任。


## Citation

如果您使用了本项目的数据或者代码，或是我们的工作对您有所帮助，请声明引用



知识微调：[Knowledge-tuning Large Language Models with Structured Medical Knowledge Bases for Trustworthy Response Generation in Chinese
](https://arxiv.org/pdf/2309.04175.pdf)

```
@article{10.1145/3686807,
author = {Wang, Haochun and Zhao, Sendong and Qiang, Zewen and Li, Zijian and Liu, Chi and Xi, Nuwa and Du, Yanrui and Qin, Bing and Liu, Ting},
title = {Knowledge-tuning Large Language Models with Structured Medical Knowledge Bases for Trustworthy Response Generation in Chinese},
year = {2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
issn = {1556-4681},
url = {https://doi.org/10.1145/3686807},
doi = {10.1145/3686807},
abstract = {Large Language Models (LLMs) have demonstrated remarkable success in diverse natural language processing (NLP) tasks in general domains. However, LLMs sometimes generate responses with the hallucination about medical facts due to limited domain knowledge. Such shortcomings pose potential risks in the utilization of LLMs within medical contexts. To address this challenge, we propose knowledge-tuning, which leverages structured medical knowledge bases for the LLMs to grasp domain knowledge efficiently and facilitate trustworthy response generation. We also release cMedKnowQA, a Chinese medical knowledge question-answering dataset constructed from medical knowledge bases to assess the medical knowledge proficiency of LLMs. Experimental results show that the LLMs which are knowledge-tuned with cMedKnowQA, can exhibit higher levels of accuracy in response generation compared with vanilla instruction-tuning and offer a new trustworthy way for the domain adaptation of LLMs. We release our code and data at .},
note = {Just Accepted},
journal = {ACM Trans. Knowl. Discov. Data},
month = aug,
keywords = {Large Language Model, Medical Question Answering, Trustworthy Response Generation, Medical Knowledge Base}
}
```

首版技术报告: [Huatuo: Tuning llama model with chinese medical knowledge](https://arxiv.org/pdf/2304.06975)

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

医学文献知识获取：[The CALLA Dataset: Probing LLMs’ Interactive Knowledge Acquisition from Chinese Medical Literature](https://arxiv.org/pdf/2309.04198.pdf)

```
@misc{du2023calla,
      title={The CALLA Dataset: Probing LLMs' Interactive Knowledge Acquisition from Chinese Medical Literature}, 
      author={Yanrui Du and Sendong Zhao and Muzhen Cai and Jianyu Chen and Haochun Wang and Yuhan Chen and Haoqiang Guo and Bing Qin},
      year={2023},
      eprint={2309.04198},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

