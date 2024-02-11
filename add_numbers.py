import json

# Read values from config.json
with open('/config/config.json') as f:
    config = json.load(f)

a = config.get('A', 10)  # Default value is 10 if 'A' key is not found
b = config.get('B', 20)  # Default value is 20 if 'B' key is not found

print(a + b)
