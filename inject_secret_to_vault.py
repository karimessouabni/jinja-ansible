import json
import hvac

def load_secrets_from_file(file_path):
    """Load secrets from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['data']

def authenticate_to_vault(client, username, password):
    """Authenticate to Vault using username and password."""
    response = client.auth.userpass.login(
        username=username,
        password=password
    )
    client.token = response['auth']['client_token']

def inject_secrets_to_vault(secrets, vault_url, vault_token, secret_path):
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
    vault_url = 'http://localhost:8200'
    username = 'your-username'  # Replace with your Vault username
    password = 'your-password'  # Replace with your Vault password
    secret_path = 'secret/data/myapp'  # Adjust the path according to your Vault setup

    client = hvac.Client(url=vault_url)
    authenticate_to_vault(client, username, password)

    secrets = load_secrets_from_file('secrets.json')
    inject_secrets_to_vault(secrets, vault_url, client.token, secret_path)

if __name__ == '__main__':
    main()
