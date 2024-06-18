import yaml
import hvac

def load_secrets_from_yaml(file_path):
    """Load secrets from a YAML file."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['data']

def inject_secrets_to_vault(vault_url, vault_token, secrets, secret_path):
    """Inject secrets into Vault."""
    client = hvac.Client(url=vault_url, token=vault_token)
    if client.is_authenticated():
        response = client.secrets.kv.v2.create_or_update_secret(
            path=secret_path,
            secret=secrets
        )
        print("Secrets injected:", response)
    else:
        print("Failed to authenticate with Vault.")

def main():
    vault_url = 'http://localhost:8200'  # Adjust if your Vault server is not running locally
    vault_token = 'your-root-token'  # Replace with your initial Vault root token
    secret_path = 'secret/data/myapp'  # Adjust the path according to your Vault setup

    secrets = load_secrets_from_yaml('secrets.yaml')
    inject_secrets_to_vault(vault_url, vault_token, secrets, secret_path)

if __name__ == '__main__':
    main()
