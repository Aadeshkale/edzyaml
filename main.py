import os
import yaml
from git import Repo

YAML_FILE_PATH = os.environ.get("INPUT_YAML_FILE_PATH")
# FILE_NAME = os.environ.get("INPUT_FILE_NAME")
YAML_KEY_PATH = os.environ.get("INPUT_YAML_KEY_PATH") # spec.template.spec.containers.0.image
YAML_VALUE = os.environ.get("INPUT_YAML_VALUE")

GIT_USERNAME = os.environ.get("INPUT_GIT_USERNAME")
GIT_TOKEN = os.environ.get("INPUT_GIT_TOKEN") 
GIT_REPO = os.environ.get("INPUT_GIT_REPO") 
GIT_USER_EMAIL = os.environ.get("INPUT_GIT_USER_EMAIL") 

# os.environ.setdefault('GIT_PYTHON_REFRESH','quiet')
dest_name = GIT_REPO






def get_updated_dict(dict_to_update, path, value):
    obj = dict_to_update
    key_list = path.split(".")
    for k in key_list[:-1]:
        if k in '0123456789':
            k = int(k)
        obj = obj[k]
    obj[key_list[-1]] = value

if __name__ == "__main__":
   
    https_url=f"https://{GIT_USERNAME}:{GIT_TOKEN}@github.com/{GIT_REPO}"
    cloned_repo = Repo.clone_from(https_url, dest_name)
    cloned_repo.config_writer().set_value("user", "name", f"{GIT_USERNAME}").release()
    cloned_repo.config_writer().set_value("user", "email", f"{GIT_USER_EMAIL}").release()

    yaml_file = f"{dest_name}/{YAML_FILE_PATH}"
    # yaml_file = f"{YAML_FILE_PATH}/{FILE_NAME}"
    data = yaml.safe_load(open(yaml_file, "rb"))
    get_updated_dict(data,YAML_KEY_PATH,YAML_VALUE)
    yaml.dump(data, open(yaml_file, "w"), default_flow_style=False)


    cloned_repo.git.add('--all')
    cloned_repo.git.commit('-m', f'edzyaml has updated {YAML_VALUE} in yaml', author=f'{GIT_USERNAME}')
    origin = cloned_repo.remote(name='origin')
    origin.push()
