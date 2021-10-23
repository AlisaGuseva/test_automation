import time


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print("Время выполнения:", t)
        return result

    return wrapper


@benchmark
def read_file(path, word):
    with open(path, "r") as file:
        word_list = [st for st in file if word in st]

    return word_list


@benchmark
def read_file2(path, word):
    with open(path, "r") as file:
        word_gen = (st for st in file if word in st)

    return word_gen

res = read_file("../files/War.txt", "мир")
res2 = read_file2("../files/War.txt", "мир")
