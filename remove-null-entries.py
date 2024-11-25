import yaml

def remove_empty_dicts(data):
    if isinstance(data, dict):
        # Recursively process each key and filter out empty dictionaries
        cleaned_dict = {k: remove_empty_dicts(v) for k, v in data.items() if v != {}}
        return cleaned_dict if cleaned_dict else None  # Remove if resulting dict is empty
    elif isinstance(data, list):
        # Recursively process lists
        cleaned_list = [remove_empty_dicts(v) for v in data if v != {}]
        return cleaned_list if cleaned_list else None  # Remove if resulting list is empty
    return data

# Load the YAML file
input_file = "input.yaml"
output_file = "output.yaml"

with open(input_file, 'r') as file:
    data = yaml.safe_load(file)

# Remove empty dictionaries
cleaned_data = remove_empty_dicts(data)

# Save the cleaned YAML
with open(output_file, 'w') as file:
    yaml.safe_dump(cleaned_data, file, default_flow_style=False)

print(f"Cleaned YAML saved to {output_file}")
