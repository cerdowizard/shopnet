import json

with open('data.json', 'r') as f:
    text = f.read()
    
    data = json.loads(text)
    for row in data:
        row["product_url"] = row["product_url"][0]


    with open('data2.json', 'w') as f:
        data = json.dumps(data, indent=4)
        f.write(data)
