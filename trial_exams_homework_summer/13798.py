from itertools import*

def f(x, y, w, z):
    return (x or ((not z) and w) or w) == (y and (not x) and w)

for i in product((0, 1), repeat=4):
    table = [
        (1, i[0], i[1], 0),
        (1, i[2], 0, 0),
        (0, 1, i[3], 1)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p,sep='')