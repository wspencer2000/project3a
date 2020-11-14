import json

with open('./symbols.json') as f:
    data = json.load(f)
    
print(data)

symbol = []
name = []



for data, value in data.items():
    symbol.append(value['ACT Symbol'])
    name.append(['Company Name'])