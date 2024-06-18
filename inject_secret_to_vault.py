import yaml
import json
import subprocess

def load_secrets_from_yaml(file_path):
    """Load secrets from a YAML file."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['secrets']

def inject_secrets_to_vault(vault_url, vault_token, secrets, secret_path):
    """Inject secrets into Vault using the REST API and curl."""
    headers = [
        f'-H "X-Vault-Token: {vault_token}"',
        '-H "Content-Type: application/json"'
    ]
    data = json.dumps({"data": secrets})
    curl_command = f'curl {" ".join(headers)} -X POST -d \'{data}\' {vault_url}/v1/{secret_path}'
    
    # Print the curl command to show the REST call
    print(f"Executing: {curl_command}")
    
    # Execute the curl command
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    
    # Print the response from the curl command
    print("Response:", result.stdout)

def main():
    vault_url = 'http://127.0.0.1:8200'  # Adjust if your Vault server is not running locally
    vault_token = 'f3b09679-3001-009d-2b80-9c306ab81aa6'  # Replace with your Vault token
    secret_path = 'secret/data/baz'  # Adjust the path according to your Vault setup

    secrets = load_secrets_from_yaml('secrets.yaml')
    inject_secrets_to_vault(vault_url, vault_token, secrets, secret_path)

if __name__ == '__main__':
    main()
