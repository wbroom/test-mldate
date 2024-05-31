import json

# 假定原始JSON文件名为 original.json
filename = 'test.json'

# 读取原始JSON文件
with open(filename, 'r', encoding='utf-8') as file:
   data = json.load(file)

# 转换数据为新的格式
transformed_data = []
for entry in data:
   # 根据gold_index的值，决定Answer是Yes还是No
   answer = 'Yes' if entry['gold_index'] == 1 else 'No'

   # 创建新的格式对象，并添加到转换后的列表中
    transformed_data.append({
        "id": entry['id'],
        "Question": entry['input'],
        "Answer": answer
    })

# 将转换后的数据输出到新的JSON文件，可以命名为transformed.json
with open('transformed.json', 'w', encoding='utf-8') as output_file:
   json.dump(transformed_data, output_file, indent=4)

print('转换完成。')
