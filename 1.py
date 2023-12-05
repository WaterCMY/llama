import json

# 指定原始 JSON 文件的路径
input_json_path = 'alpaca_data.json'  # 更改为您的文件路径

# 指定新 JSON 文件的路径
output_json_path = 'alpaca_data_200.json'  # 更改为您想要的文件路径

# 打开并读取原始 JSON 文件
with open(input_json_path, 'r') as file:
    data = json.load(file)

# 截取前200条数据
data_subset = data[:200]

# 写入新的 JSON 文件
with open(output_json_path, 'w') as file:
    json.dump(data_subset, file, indent=4)
