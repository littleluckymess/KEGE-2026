from itertools import permutations, product

def f(x, y, w, z):
    return (w == z) or (not(y <= w)) or (not x)

for i in product((0, 1), repeat=5):
    table = [
        (i[0], 0, 1, 0),
        (i[1], 1, 1, i[2]),
        (0, i[3],i[4], 0)
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')