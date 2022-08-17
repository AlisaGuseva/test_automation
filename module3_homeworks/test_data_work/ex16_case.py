import json
from csv import DictReader

books_dict_ref = {"Title": None, "Author": None, "Pages": None, "Genre": None}
users_dikt = {"name": None, "gender": None, "address": None, "age": None, "books": [] }


def gen_func_book(books_dict):  # Возвращаем 1 словарь для цикла КНИГИ
    for i in books_dict:
        for key, value in i.items():
            if "Title" in key or "Author" in key or "Pages" in key or "Genre" in key:
                books_dict_ref[key] = value
        yield books_dict_ref


def gen_func_users(user_read):  # Возвращаем 1 словарь для цикла ПОЛЬЗОВАТЕЛИ
    for list_user in user_read:
        for dictionary_user, dict_value in list_user.items():
            if "name" in dictionary_user or "gender" in dictionary_user or "address" in dictionary_user or "age" in dictionary_user:
                users_dikt[dictionary_user] = dict_value
        yield users_dikt


with open("users.json", "r") as users, open("books.csv", "r") as books, open(
        "result.json", "w") as library:  # ОТКРЫВАЕМ ВСЕ НУЖНЫЕ ФАЙЛЫ В МЕНЕДЖЕРЕ КОНТЕКСТА
    user_str = users.read()
    user_read = json.loads(user_str)  # С читываем json построчно
    us_list = []  # словарь для цикла

    for i in gen_func_users(user_read):  # Заполняем список словорями Пользователи
        us_list.append(users_dikt.copy())

    books_lst = DictReader(books)  # считываем csv + создаем словари
    bk_list = []  # словарь для цикла

    for i in gen_func_book(books_lst):  # Заполняем список словорями Книги
        bk_list.append(books_dict_ref.copy())

    count = 0
    print(len(us_list))
    for i in bk_list:
        if count == len(us_list):  # перезапускаем цикл по пользователям
            count = 0
            print("count0")
        else:
            (us_list[count])["books"].append(i)
            print(us_list[count])
            count = count + 1
           # if "books" not in us_list[count]:
           #     (us_list[count])["books"] = []  # создаем новый список, для каждого пользователя
           #     (us_list[count])["books"].append(i)
           #     print(us_list[count])
           #     count = count + 1
           # else:


    json.dump(us_list, library, indent=4)