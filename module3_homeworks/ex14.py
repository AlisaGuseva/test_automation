import json
from csv import DictReader
import time

books_file = "books.csv"
users_file = "users.json"
result_file = "result.json"

USER_ATTRS = ('name', 'gender', 'address', 'age', 'books')
BOOK_ATTRS = ('title', 'author', 'pages', 'genre')


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print('Время выполнения:', t)
        return result

    return wrapper


def tryconvert(*types):
    def convert(value):
        for t in types:
            try:
                return t(value)
            except (ValueError, TypeError):
                continue
        return value
    return convert


def gen_csv(file):
    with open(file, newline='', mode='r') as f:
        for d in DictReader(f):
            yield {k.lower(): tryconvert(int)(v)
                   for k, v in d.items() if k.lower() in BOOK_ATTRS}


def gen_json(file):
    with open(file, mode='r') as f:
        for entry in json.load(f):
            entry['books'] = []
            yield {k: v for k, v in entry.items() if k in USER_ATTRS}


@benchmark
def ex14():
    i = 0
    total_books = 0
    users = list(gen_json(users_file))
    for b in gen_csv(books_file):
        try:
            t = users[i]
        except IndexError:
            i = 0
        users[i]['books'].append(b)
        total_books += 1
        i += 1
    del i

    with open(result_file, mode='w') as f:
        try:
            json.dump(users, f, indent=4)
        except Exception as e:
            print(e)
        else:
            print(
                f"{total_books} books have been distributed among {len(users)} users")


ex14()
