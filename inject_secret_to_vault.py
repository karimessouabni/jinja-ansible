import yaml
import hvac

def load_secrets_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        return data['secrets']

def inject_secrets_to_vault(secrets, vault_url, vault_token, secrets_path):
    client = hvac.Client(url=vault_url, token=vault_token)
    for path, secrets_data in secrets.items():
        full_path = f'{secrets_path}/{path}'
        client.secrets.kv.v2.create_or_update_secret(path=full_path, secret=secrets_data)
        print(f"Injected secrets into {full_path}")

def main():
    yaml_file_path = 'secrets.yaml'
    vault_url = 'http://localhost:8200'
    vault_token = 'your_vault_token_here'
    secrets_path = 'mysecrets'  # This is the base path where secrets will be stored in Vault

    secrets = load_secrets_from_yaml(yaml_file_path)
    inject_secrets_to_vault(secrets, vault_url, vault_token, secrets_path)

if __name__ == '__main__':
    main()
