import time
import json
from csv import DictReader


def benchmark(func):

    def wrapper(*args: object, **kwargs: object) -> object:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print('Время выполнения:', t)
        return result

    return wrapper


@benchmark
def func_ex2():
    with open('books.csv', newline='') as f:
        reader = DictReader(f)
        books = []
        for row in reader:
            del row['Publisher']
            books.append(row)

    with open('users.json', 'r') as file:
        users = json.load(file)
        res_users = []

    for element in users:
        res_users.append({"name": element["name"],
                          "gender": element["gender"],
                          "address": element["address"],
                          "age": element["age"], "books": []})

    j = 0

    for i in range(len(books)):
        if j == len(res_users):
            j = 0
        res_users[j]['books'].append(books[i])
        j += 1

    with open('result.json', 'w') as f:
        new_j = json.dumps(res_users, indent=4)
        f.write(new_j)


func_ex2()


