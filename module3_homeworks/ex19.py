import csv
import json
import random


def books_csv():
    with open("../test_data/books.csv") as f:
        reader = csv.reader(f)
        header = next(reader)
        books = [dict(zip(header, row)) for row in reader]
        custom_books = []
    for book in books:
        book = {
            'title': book['Title'],
            'author': book['Author'],
            'pages': book['Pages'],
            'genre': book['Genre']
        }
        custom_books += [book]
    return custom_books


def users_json():
    with open("../test_data/users.json", "r") as file:
        users = json.loads(file.read())
        res_users = []
        for user in users:
            res_user = {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': []
            }
            res_users += [res_user]
    return res_users


def distribute_books(books_list, users_list):
    for _ in books_list:
        for user in users_list:
            if len(books_list) == 0:
                return users_list
            random_book = random.choice(books_list)
            user['books'].append(random_book)
            books_list.remove(random_book)
    return users_list


def write_result(data):
    with open("../src/result.json", 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    users = users_json()
    books = books_csv()

    res_users = distribute_books(books_list=books, users_list=users)