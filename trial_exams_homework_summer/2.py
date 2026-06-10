from itertools import*

def f(x, y, w, z):
    return (not(y <= (x == z))) and (w <= x)

for i in product((0,1), repeat=7):
    table = [
        (i[0], 0, 0, i[1]),
        (0, i[2], 0, i[3]),
        (i[4], 1, i[5], i[6])
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')