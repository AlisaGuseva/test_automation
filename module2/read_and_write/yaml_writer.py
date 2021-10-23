import yaml

login = "alisa"
kafka = {
    'caRootLocation': 'certs//kafka-ca-root.crt',
    'certLocation': 'certs//kafka-client.crtt',
    'keyLocation': 'certs//kafka-client.pem'
}

to_yaml = {'login': login, 'kafka': kafka}

with open('../files/example_write.yaml', 'w') as f:
    yaml.dump(to_yaml, f, default_flow_style=False)

with open('../files/example_write.yaml') as f:
    print(f.read())

