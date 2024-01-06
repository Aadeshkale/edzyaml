import os
import yaml



file_path = os.getenv("file_path")
file_name = os.getenv("file_name")
yaml_key = os.getenv("yaml_key") # spec.template.spec.image.containers.0.image
yaml_value = os.getenv("yaml_value")

yaml_file = f"{file_path}/{file_name}"
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
    get_updated_dict(data,yaml_key,yaml_value)
    yaml.dump(data, open(yaml_file, "w"), default_flow_style=False)
    