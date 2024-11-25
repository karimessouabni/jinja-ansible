import yaml

def remove_nulls(data):
    if isinstance(data, dict):
        return {k: remove_nulls(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [remove_nulls(v) for v in data if v is not None]
    return data

# Load the YAML file
input_file = "input.yaml"
output_file = "output.yaml"

with open(input_file, 'r') as file:
    data = yaml.safe_load(file)

# Remove null entries
cleaned_data = remove_nulls(data)

# Save the cleaned YAML
with open(output_file, 'w') as file:
    yaml.safe_dump(cleaned_data, file, default_flow_style=False)

print(f"Cleaned YAML saved to {output_file}")
