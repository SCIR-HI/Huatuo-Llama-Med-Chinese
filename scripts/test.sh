#!/bin/sh

# If inferring with the llama model, set 'use_lora' to 'False' and 'prompt_template' to 'ori_template'.
# If inferring with the default alpaca model, set 'use_lora' to 'True', 'lora_weights' to 'tloen/alpaca-lora-7b', and 'prompt_template' to 'alpaca'.
# If inferring with the llama-med model, download the LORA weights and set 'lora_weights' to './lora-llama-med' (or the exact directory of LORA weights) and 'prompt_template' to 'med_template'.

BASE_MODEL="decapoda-research/llama-7b-hf"
# 原始llama
o_cmd="python infer.py \
    --base_model ${BASE_MODEL} \
    --use_lora False \
    --prompt_template 'ori_template'"

# Alpaca
a_cmd="python infer.py \
    --base_model ${BASE_MODEL} \
    --use_lora True \
    --lora_weights "tloen/alpaca-lora-7b" \
    --prompt_template 'alpaca'"

# llama-med
m_cmd="python infer.py \
    --base_model ${BASE_MODEL} \
    --use_lora True \
    --lora_weights "lora-llama-med" \
    --prompt_template 'med_template'"

echo "ori"
eval $o_cmd > infer_result/o_tmp.txt
echo "alpaca"
eval $a_cmd > infer_result/a_tmp.txt
echo "med"
eval $m_cmd > infer_result/m_tmp.txt