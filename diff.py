import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_keys(data, parent_key=''):
    keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keys.append(full_key)
            if isinstance(value, dict):
                keys.extend(get_keys(value, full_key))
    return keys

def compare_keys(yaml1, yaml2):
    keys1 = set(get_keys(yaml1))
    keys2 = set(get_keys(yaml2))

    keys_only_in_yaml1 = keys1 - keys2
    keys_only_in_yaml2 = keys2 - keys1

    return keys_only_in_yaml1, keys_only_in_yaml2

def write_differences_to_file(file_path, keys_only_in_yaml1, keys_only_in_yaml2):
    with open(file_path, 'w') as file:
        if keys_only_in_yaml1:
            file.write("Keys only in the first YAML file:\n")
            for key in sorted(keys_only_in_yaml1):
                file.write(f"{key}\n")
        if keys_only_in_yaml2:
            file.write("\nKeys only in the second YAML file:\n")
            for key in sorted(keys_only_in_yaml2):
                file.write(f"{key}\n")

def main(yaml_file1, yaml_file2, output_file):
    yaml1 = load_yaml(yaml_file1)
    yaml2 = load_yaml(yaml_file2)

    keys_only_in_yaml1, keys_only_in_yaml2 = compare_keys(yaml1, yaml2)

    write_differences_to_file(output_file, keys_only_in_yaml1, keys_only_in_yaml2)

if __name__ == "__main__":
    yaml_file1 = "file1.yaml"
    yaml_file2 = "file2.yaml"
    output_file = "differences.txt"
    
    main(yaml_file1, yaml_file2, output_file)
