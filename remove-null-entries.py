import yaml

def clean_yaml(data):
    if isinstance(data, dict):
        # Process dictionary keys and remove null values or empty dictionaries
        cleaned_dict = {
            k: clean_yaml(v) for k, v in data.items() if v is not None and v != {}
        }
        return cleaned_dict if cleaned_dict else None  # Remove if resulting dict is empty
    elif isinstance(data, list):
        # Process lists and remove null values or empty dictionaries
        cleaned_list = [clean_yaml(v) for v in data if v is not None and v != {}]
        return cleaned_list if cleaned_list else None  # Remove if resulting list is empty
    return data

# Load the YAML file
input_file = "input.yaml"
output_file = "output.yaml"

with open(input_file, 'r') as file:
    data = yaml.safe_load(file)

# Clean the data by removing nulls and empty dictionaries
cleaned_data = clean_yaml(data)

# Save the cleaned YAML
with open(output_file, 'w') as file:
    yaml.safe_dump(cleaned_data, file, default_flow_style=False)

print(f"Cleaned YAML saved to {output_file}")
