from itertools import*

def f(x, y, w, z):
    return (z <= (not y <= x)) or w

for i in product((0, 1), repeat=7):
    table = [
        (i[0], 1, i[1], i[2]),
        (i[3], i[4], 0, 0),
        (i[5], 0, 1, i[6])
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [0, 0, 0]:
                print(*p,sep='')