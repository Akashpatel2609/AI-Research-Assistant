import os
import shutil
from huggingface_hub import hf_hub_download, HfApi

def download_dataset_dir(repo_id, dir_path, local_dir="hf_dataset"):
    os.makedirs(local_dir, exist_ok=True)
    files = HfApi().list_repo_files(repo_id=repo_id, repo_type="dataset")
    for file in files:
        if file.startswith(dir_path):
            path = hf_hub_download(repo_id=repo_id, filename=file, repo_type="dataset")
            target = os.path.join(local_dir, file.replace("/", "_"))
            shutil.move(path, target)
            print(f"Downloaded: {file} → {target}")

# Example usage
dir_list = ['ComputerScience,2022-2022']

# dir_list = ['ComputerScience,1970-2008', 'ComputerScience,2009-2011', 'ComputerScience,2012-2013',
#            'ComputerScience,2014-2015', 'ComputerScience,2016-2016', 'ComputerScience,2017-2017',
#            'ComputerScience,2018-2018', 'ComputerScience,2019-2019', 'ComputerScience,2020-2020',
#            'ComputerScience,2021-2021', 'ComputerScience,2022-2022']

for i in dir_list:
    download_dataset_dir(repo_id="claran/modular-s2orc", dir_path=i, local_dir="hf_files")