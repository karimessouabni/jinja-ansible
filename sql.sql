#!/bin/bash

# Database credentials
DB_USER="your_user"
DB_PASSWORD="your_password"
DB_NAME="your_database"
DB_HOST="localhost"

# YAML file path
YAML_FILE="path_to_your_file.yaml"

# Initialize an array to hold the values
declare -a names

# Read the YAML file and extract values
while IFS= read -r line; do
    name=$(echo "$line" | awk '{print $2}')
    names+=("('$name', '$name')")
done < <(grep 'name:' $YAML_FILE)

# Join all array elements into a single string, separated by commas
value_string=$(IFS=,; echo "${names[*]}")

# Full SQL command to insert all the entries
sql="INSERT INTO environment (env_id, env_name) VALUES $value_string;"

echo "Executing SQL command..."
mysql -h $DB_HOST -u $DB_USER -p"$DB_PASSWORD" $DB_NAME -e "$sql"

echo "Data injection complete."
