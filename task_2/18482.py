from itertools import product, permutations
def f(x,y,w,z):
    return (x ==(y <=(z or x))) and w

for i in product((0,1), repeat=5):
    table = [
        (1, 0, 1, i[0]),
        (0, i[1], i[2], 0),
        (1, 0, i[3], i[4])
    ]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p, sep='')

