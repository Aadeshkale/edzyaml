import os
import yaml
from git import Repo

FILE_PATH = os.environ.get("INPUT_FILE_PATH")
# FILE_NAME = os.environ.get("INPUT_FILE_NAME")
YAML_KEY = os.environ.get("INPUT_YAML_KEY") # spec.template.spec.containers.0.image
YAML_VALUE = os.environ.get("INPUT_YAML_VALUE")

USERNAME = os.environ.get("INPUT_USERNAME")
GIT_TOKEN = os.environ.get("INPUT_GIT_TOKEN") 
GIT_REPO = os.environ.get("INPUT_GIT_REPO") 


https_url=f"https://{USERNAME}:{GIT_TOKEN}@github.com/{GIT_REPO}"
dest_name = GIT_REPO
cloned_repo = Repo.clone_from(https_url, dest_name)




yaml_file = f"{dest_name}/{FILE_PATH}"
# yaml_file = f"{FILE_PATH}/{FILE_NAME}"
data = yaml.safe_load(open(yaml_file, "rb"))

def get_updated_dict(dict_to_update, path, value):
    obj = dict_to_update
    key_list = path.split(".")
    for k in key_list[:-1]:
        if k in '0123456789':
            k = int(k)
        obj = obj[k]
    obj[key_list[-1]] = value

if __name__ == "__main__":
    get_updated_dict(data,YAML_KEY,YAML_VALUE)
    yaml.dump(data, open(yaml_file, "w"), default_flow_style=False)
    cloned_repo.git.add('--all')
    cloned_repo.git.commit('-m', f'edzyaml has updated {YAML_VALUE} in yaml', author=f'{USERNAME}')
    origin = cloned_repo.remote(name='origin')
    origin.push()
