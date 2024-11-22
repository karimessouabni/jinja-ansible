import yaml

def load_yaml(file_path):
    """Charge un fichier YAML et retourne le contenu sous forme de dictionnaire."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def normalize_data(data):
    """
    Normalise les données YAML :
    - Trie les dictionnaires par clé.
    - Supprime les entrées vides dans les listes.
    """
    if isinstance(data, dict):
        return {key: normalize_data(value) for key, value in sorted(data.items())}
    elif isinstance(data, list):
        return [normalize_data(item) for item in data if item]  # Ignore les entrées vides
    else:
        return data

def compare_yaml(file1, file2):
    """Compare deux fichiers YAML après normalisation."""
    yaml1 = load_yaml(file1)
    yaml2 = load_yaml(file2)

    normalized_yaml1 = normalize_data(yaml1)
    normalized_yaml2 = normalize_data(yaml2)

    return normalized_yaml1 == normalized_yaml2

# Exemple d'utilisation
file1 = 'fichier1.yaml'
file2 = 'fichier2.yaml'

if compare_yaml(file1, file2):
    print("Les fichiers YAML sont identiques (ordre et entrées vides ignorés).")
else:
    print("Les fichiers YAML sont différents.")