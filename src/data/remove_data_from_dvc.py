

import os
from glob import glob

# Specify folders
data_dirs = ["Training_Batch_files","Prediction_Batch_files"]

for data_dir in data_dirs:
    files = glob(os.path.join('data', data_dir) + r"/*.dvc")
    for filePath in files:
        os.remove(filePath)

print("\n #### all files removed from dvc ####")