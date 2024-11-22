import yaml
from deepdiff import DeepDiff

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

def get_yaml_differences(file1, file2):
    """Retourne les différences entre deux fichiers YAML normalisés."""
    yaml1 = normalize_data(load_yaml(file1))
    yaml2 = normalize_data(load_yaml(file2))

    # Utilisation de DeepDiff pour trouver les différences
    differences = DeepDiff(yaml1, yaml2, ignore_order=True).to_dict()
    return differences

def save_differences_to_yaml(differences, output_file):
    """Sauvegarde les différences dans un fichier YAML."""
    with open(output_file, 'w', encoding='utf-8') as file:
        yaml.dump(differences, file, allow_unicode=True, default_flow_style=False)

# Exemple d'utilisation
file1 = 'fichier1.yaml'
file2 = 'fichier2.yaml'
output_file = 'differences.yaml'

differences = get_yaml_differences(file1, file2)

if differences:
    save_differences_to_yaml(differences, output_file)
    print(f"Les différences ont été sauvegardées dans {output_file}.")
else:
    print("Les fichiers YAML sont identiques.")
