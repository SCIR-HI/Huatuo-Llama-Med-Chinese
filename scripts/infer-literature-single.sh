#!/bin/sh

# If inferring with the llama model, set 'use_lora' to 'False' and 'prompt_template' to 'ori_template'.
# If inferring with the default alpaca model, set 'use_lora' to 'True', 'lora_weights' to 'tloen/alpaca-lora-7b', and 'prompt_template' to 'alpaca'.
# If inferring with the llama-med model, download the LORA weights and set 'lora_weights' to './lora-llama-med' (or the exact directory of LORA weights) and 'prompt_template' to 'med_template'.

"""单轮"""
python infer_literature.py \
    --base_model 'decapoda-research/llama-7b-hf' \
    --lora_weights './lora-llama-literature' \
    --single_or_multi 'single' \
    --use_lora True \
    --prompt_template 'literature_template'
