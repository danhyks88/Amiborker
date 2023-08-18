import pandas as pd
import json

# Đường dẫn tới tệp JSON
json_file_path = "D:/Github/ChungKhoan/Data/Export/FPT.json"

# Đọc dữ liệu từ tệp JSON
with open(json_file_path, 'r') as json_file: 
    json_data = json.load(json_file)

# Tạo DataFrame từ dữ liệu JSON
df = pd.DataFrame.from_dict(json_data, orient='index')

# In kết quả
print(df)
