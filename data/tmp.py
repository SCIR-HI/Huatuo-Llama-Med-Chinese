import json

# 假设数据存储在 data.json 文件中
data = []
with open('llama_data.json', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        data.append(json.loads(line))

# 遍历每个对象，找到 output 属性不为字符串类型的对象
new_data = []
for obj in data:
    if isinstance(obj['output'], str):
        new_data.append(obj)
with open("llama_data_1.json","w") as f:
    for n in new_data:
        f.write(json.dumps(n,ensure_ascii=False))
        f.write("\n")