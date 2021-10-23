list1 = [-2, -1, 0, 1, 2]

l_new = []
for i in list1:
    if i >= 0:
        l_new.append(i*2)


def gen_func(args):
    for a in args:
        if a >= 0:
            yield a*2

#list_comp = [i*2 for i in list1 if i >= 0]
#print(id(list_comp) == id(list1))
#print("====")
#print(type(list_comp))
#print(list_comp)

gen_exp = (i*2 for i in list1 if i >= 0)

print(type(gen_func(list1)))
s = gen_func(list1)
print(next(s))
print(next(s))
print(next(s))
print(next(s))

for i in gen_exp:
    pass
    #print("i'm from for")
    #print(i)

for i in gen_exp:
    pass
    #print("hello")
    #print(i)
