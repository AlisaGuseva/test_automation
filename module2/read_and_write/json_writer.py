import json

data = {
    "users": [
        {"login": "Alisa", "email": "alisa.april.one@gmail.ru"},
        {"login": "Plaksa", "email": "cat@gmail.ru"},
        {"login": "MMayers", "email": "fromhellwithlove@gmail.com"},
    ]
}

with open("example.json", "w") as f:
    s = json.dumps(data, indent=4)
    f.write(s)
