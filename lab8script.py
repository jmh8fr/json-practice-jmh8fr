#!/usr/bin/python3

import json

file_path = '/workspace/json-practice-jmh8fr/data/schacon.repos.json'
output_csv_path = 'chacon.csv'

with open(file_path, 'r') as file:
    data = json.load(file)

with open(output_csv_path, 'w') as csv_file:

    for entry in data[:5]:
        name = entry['name']
        html_url = entry['html_url']
        updated_at = entry['updated_at']
        visibility = entry['visibility']
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(line)
print(f"Data successfully written to {output_csv_path}")
