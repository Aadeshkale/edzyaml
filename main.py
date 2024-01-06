import os
import yaml



file_path = os.getenv("file_path")
file_name = os.getenv("file_name")
yaml_key = os.getenv("yaml_key") # spec.template.spec.image
yaml_value = os.getenv("yaml_value")

with open(f"{file_path}/{file_name}",'r+') as file:
    contents = yaml.safe_load(file)
    print(contents["spec"]["template"])
    if '.' in yaml_key:
        key_path = []
        rst = yaml_key.split('.')
        print(rst)

if __name__ == "__main__":
    print("Processing...")