import time
import json
import csv
import pytest


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print('Время выполнения:', t)
        return result

    return wrapper


"""
def test_check_json_format():
    with open("result.json", "r") as json_file:
        try:
            print(json.load(json_file))
        except json.decoder.JSONDecodeError:
            pytest.fail("Ошибка чтения json", json.decoder.JSONDecodeError)

"""


def read_users_from_json(file_name):
    with open(file_name, "r") as users_file:
        return json.load(users_file)


def read_books_from_csv(file_name):
    with open(file_name, "r") as books_file:
        books_file = csv.reader(books_file)
        header = [column_name.lower() for column_name in next(books_file)]
        books_list = []
        for row in books_file:
            books_list.append(dict(zip(header, row)))
        return books_list


def write_result_in_json(file_name, values):
    with open(file_name, "w") as result_file:
        result_file.write(json.dumps(values, indent=4))


class UserLibrary:
    def __init__(self, name, gender, address, age):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = []

    def add_book(self, book_item):
        self.books.append(book_item)


@benchmark
def func_ex7():
    users = read_users_from_json("users.json")
    users_list = [UserLibrary(user["name"],
                              user["gender"],
                              user["address"],
                              user["age"])
                  for user in users]
    users_list_len = len(users_list)
    books = read_books_from_csv("books.csv")
    for i in range(len(books)):
        del(books[i]["publisher"])
        users_list[i % users_list_len].add_book(books[i])

    write_result_in_json("result.json", [user.__dict__ for user in users_list])


func_ex7()


