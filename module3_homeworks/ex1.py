import json
import csv

import numpy as np

import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print('Время выполнения:', t)
        return result

    return wrapper


def get_people_data(person):
    return {
        "name": person.get("name"),
        "gender": person.get("gender"),
        "address": person.get("address"),
        "age": person.get("age")
    }


def get_book_data(book):
    return {
        "title": book.get("Title"),
        "author": book.get("Author"),
        "pages": book.get("Pages"),
        "genre": book.get("Genre")
    }


def get_equals_books(books: list, people_count: int):
    for item in np.array_split(books, people_count):
        # print(20*"==")
        # print(list(item))
        # print(20 * "==")
        yield list(item)


def add_books_to_people(people: dict, equal_books: list):
    people["books"] = equal_books
    return people


@benchmark
def func_ex1():
    people_list = []
    books_list = []
    people_with_books = []

    with open("users.json", "r") as file:
        people = json.load(file)
    for person in people:
        people_list.append(get_people_data(person))

    with open("books.csv", "r") as file:
        books = list(csv.DictReader(file))
    for book in books:
        books_list.append(get_book_data(book))

    equals_books_gen = get_equals_books(books_list, len(people_list))

    for person in people_list:
        people_with_books.append(add_books_to_people(person, next(equals_books_gen)))

    with open("result.json", "w") as outfile:
        json.dump(people_with_books, outfile, indent=4)


func_ex1()
