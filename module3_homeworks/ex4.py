import time
import json
import csv
from csv import DictReader


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print('Время выполнения:', t)
        return result

    return wrapper


@benchmark
def func_ex4():
    reference_users = ['name', 'gender', 'address', 'age']
    users_list = []
    new_dict = {}
    reference_users_list = []
    with open("users.json", "r") as f:
        users = json.loads(f.read())


    # укладываю юзеров в шаблонный вид
    for user in users:
        users_list.append(user)
    for i in range(len(users_list)):
        users_dict = {j: users_list[i][j] for j in reference_users if j in users_list[i].keys()}
        reference_users_list.append(users_dict)

    # объявляю списки/словари, читаю csv
    reference_books = ["Title", "Author", "Genre", "Pages"]
    books_list = []
    reference_books_list = []
    with open('books.csv', newline='') as f:
        reader = DictReader(f)
        for row in reader:
            books_list.append(row)

    # укладываю книжки в шаблонный вид
    for i in range(len(books_list)):
        users_dict = {k: v for k, v in books_list[i].items() if k in reference_books}
        reference_books_list.append(users_dict)

    # попытка уложить книжки по пользователям
    count = 0
    count_i = 0

    for i in range(len(reference_users_list)):
        c = (len(reference_books_list) - count) // len(reference_users_list)
        if (len(reference_books_list) - count) % len(reference_users_list) != 0:
            c += 1
            count += 1

        reference_users_list[i]['books'] = []

        for j in reference_books_list[count_i: count_i + c]:
            reference_users_list[i]['books'].append(j)
        count_i += c

    # укладываю все в json файл
    with open("example.json", "w") as f:
        s = json.dumps(reference_users_list, indent=4)
        f.write(s)


func_ex4()

