import numpy as np
import os



# 1. 确保在当前目录创建 emb_data 文件夹
os.makedirs('emb_data', exist_ok=True)

# 2. 制造 1KB 的合法空字典假文件
dummy_data = {}
files_to_mock = ['topic_data.npy', 'user_data.npy', 'post_data.npy']

for file_name in files_to_mock:
    file_path = os.path.join('emb_data', file_name)
    np.save(file_path, dummy_data)
    

# 3. 顺手建几个空文件夹，防止程序检测目录时报错
empty_folders = ['topic_data', 'user_data', 'post_data', 'raw_data']
for folder in empty_folders:
    os.makedirs(folder, exist_ok=True)
    

