from itertools import product, permutations

def f(x,y,w,z):
    return ((z == x) <= w) and (w <=(y and x))

for i in product((0, 1), repeat=3):
    table = [
        (1, 1, i[0], 0),
        (1, i[1], i[2], 0),
        (1, 0, 1, 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')