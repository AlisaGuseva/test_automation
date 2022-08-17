import time
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


def get_book_data(book):
    return {
        "title": book.get("Title"),
        "author": book.get("Author"),
        "pages": book.get("Pages"),
        "genre": book.get("Genre")
    }


@benchmark
def func_with_del1():
    with open('books.csv', newline='') as f:
        reader = DictReader(f)
        books = []
        for row in reader:
            del row['Publisher']
            books.append(row)


@benchmark
def func_with_del2():
    with open('books.csv', newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        books = []
        for row in reader:
            del row[4]
            books.append(dict(zip(header, row)))


@benchmark
def func_with_add1():
    books_list = []
    with open("books.csv", "r") as file:
        books = list(csv.DictReader(file))
    for book in books:
        books_list.append(get_book_data(book))


@benchmark
def func_with_add2():
    with open('books.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        csv_list = []
        for row in reader:
            csv_list.append(dict(zip(header, row)))


@benchmark
def func_with_del3():
    with open('books.csv', newline='') as f:
        reader = DictReader(f)
        book_mas = []
        for row in reader:
            book_mas.append(row)
        books = []
        for i in range(len(book_mas)):
            book = {'title': book_mas[i]['Title'],
                    'author': book_mas[i]['Author'],
                    'pages': int(book_mas[i]['Pages']),
                    'genre': book_mas[i]['Genre']}
            books.append(book)
            del book


func_with_add1()
func_with_add2()
func_with_del1()
func_with_del2()
func_with_del3()






