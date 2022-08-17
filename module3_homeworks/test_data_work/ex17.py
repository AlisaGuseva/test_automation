import json
import csv

result = []

with open('users.json', 'r') as f:
    users = json.load(f)
    for user in users:
        result.append(
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': []
            }
        )

with open('books.csv', 'r') as f:
    books = csv.DictReader(f)
    i = 0

    for book in books:
        result[i % len(result)]['books'].append(
            {
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre']
            }
        )
        i += 1

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4)