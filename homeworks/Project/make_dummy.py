import numpy as np
import os



# 1. Make sure to create the "emb_data" folder in the current directory.
os.makedirs('emb_data', exist_ok=True)

# 2. Create a 1KB dummy file of an empty dictionary
dummy_data = {}
files_to_mock = ['topic_data.npy', 'user_data.npy', 'post_data.npy']

for file_name in files_to_mock:
    file_path = os.path.join('emb_data', file_name)
    np.save(file_path, dummy_data)
    

# 3. Create several empty folders to prevent the program from generating errors when it detects the directory.
empty_folders = ['topic_data', 'user_data', 'post_data', 'raw_data']
for folder in empty_folders:
    os.makedirs(folder, exist_ok=True)
    


