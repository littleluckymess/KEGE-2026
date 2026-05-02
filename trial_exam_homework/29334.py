from itertools import product, permutations

def f(x, y, w, z):
    return ((z <= x) <= (x == y)) or (not w)

for i in product((0, 1), repeat=5):
    table = [
        (i[0], 0, 1, 0),
        (0, i[1],i[2], 0),
        (i[3], 1, 1, i[4])
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')