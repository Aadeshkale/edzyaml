import os
import yaml



FILE_PATH = os.environ.get("INPUT_FILE_PATH")
FILE_NAME = os.environ.get("FILE_NAME")
YAML_KEY = os.environ.get("INPUT_YAML_KEY") # spec.template.spec.containers.0.image
YAML_VALUE = os.environ.get("INPUT_YAML_VALUE")

yaml_file = f"{FILE_PATH}/{FILE_NAME}"
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
    