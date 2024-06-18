import yaml
import hvac

def load_secrets_from_yaml(file_path):
    """Load secrets from a YAML file."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['data']

def authenticate_to_vault(client, username, password):
    """Authenticate to Vault using username and password."""
    response = client.auth.userpass.login(
        username=username,
        password=password
    )
    client.token = response['auth']['client_token']

def inject_secrets_to_vault(client, secrets, secret_path):
    """Inject secrets into Vault."""
    if client.is_authenticated():
        response = client.secrets.kv.v2.create_or_update_secret(
            path=secret_path,
            secret=secrets
        )
        print("Secrets injected:", response)
    else:
        print("Failed to authenticate with Vault.")

def main():
    vault_url = 'http://localhost:8200'
    username = 'your-username'  # Replace with your Vault username
    password = 'your-password'  # Replace with your Vault password
    secret_path = 'secret/data/myapp'  # Adjust the path according to your Vault setup

    client = hvac.Client(url=vault_url)
    authenticate_to_vault(client, username, password)

    secrets = load_secrets_from_yaml('secrets.yaml')
    inject_secrets_to_vault(client, secrets, secret_path)

if __name__ == '__main__':
    main()
