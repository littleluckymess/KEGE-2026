from itertools import product, permutations

def f(x,y,w,z):
    return (x and (not y)) or (x == z) or w

for i in product((0, 1), repeat=4):
    table = [
        (i[0], i[1], 0, 1),
        (1, 0, i[2], 1),
        (1, 1, 0, i[3])
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')