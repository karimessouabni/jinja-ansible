#!/bin/bash

# Database credentials
DB_USER="your_user"
DB_PASSWORD="your_password"
DB_NAME="your_database"
DB_HOST="localhost"

# YAML file path
YAML_FILE="path_to_your_file.yaml"

# Read the YAML file and extract values
grep 'name:' $YAML_FILE | awk '{print $2}' | while read name; do
  echo "Inserting $name into database..."
  # MySQL command to insert the data into the database
  mysql -h $DB_HOST -u $DB_USER -p"$DB_PASSWORD" $DB_NAME -e "INSERT INTO environment (env_id, env_name) VALUES ('$name', '$name');"
done

echo "Data injection complete."
