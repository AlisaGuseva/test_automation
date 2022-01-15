list1 = [-2, -1, 0, 1, 2]


def gen_func(args):
    for a in args:
        if a >= 0:
            yield a*2


gen_res = gen_func(list1)
print(gen_res)

#print(next(gen_res))
#print(next(gen_res))
#print(next(gen_res))
#print(next(gen_res))

for i in gen_res:
    print(i)

#for i in gen_res:
#    print(i)