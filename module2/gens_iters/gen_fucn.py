
def gen_func(args):
    for a in args:
        if a >= 0:
            yield a*2


list1 = [-2, -1, 0, 1, 2]

res = gen_func(list1)
print(res)

print(next(res))
print(next(res))
print(next(res))

