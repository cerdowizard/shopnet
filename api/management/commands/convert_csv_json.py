import csv
import json

csv_file = 'csv_files/Nordstrom Rack - Sheet1.csv'
json_file = 'nordstrom.json'

data = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)
