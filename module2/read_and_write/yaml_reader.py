import yaml

with open('../files/example.yaml') as f:
    templates = yaml.safe_load(f)

print(templates)


