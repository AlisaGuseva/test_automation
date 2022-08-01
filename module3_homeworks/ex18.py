
import json
from csv import DictReader


def gen_func(args):
    for element in args:
        yield element


def collect_users(path):
    with open(path, 'r') as json_file:
        users = json.loads(json_file.read())
        user_info = [{'name': user['name'], 'gender': user['gender'], 'address': user['address'], 'age': user['age'],
                      'books': []} for user in users]
    return [user_info, len(user_info)]


def collect_books(path):
    with open(path, newline='') as csv_file:
        books = DictReader(csv_file)

        book_info = [{'title': row['Title'], 'author': row['Author'], 'pages': int(row['Pages']), 'genre': row['Genre']}
                     for row in books]
        return [book_info, len(book_info)]


def merge_users_and_books():
    user_info, user_len = collect_users(path='users.json')
    book_info, book_len = collect_books(path='books.csv')
    book_info = gen_func(book_info)

    for user in range(user_len):
        for i in range(book_len // user_len):
            user_info[user]['books'].append(next(book_info))
        if user < book_len % user_len:
            user_info[user]['books'].append(next(book_info))

    return user_info


def write_reference(path):
    with open(path, "w") as file:
        file.write(json.dumps(merge_users_and_books(), indent=4))


write_reference(path='reference.json')
