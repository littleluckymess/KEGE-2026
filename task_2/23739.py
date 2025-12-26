from itertools import product, permutations

def f(x,y,z,w):
    return (x or y) and not (y == z) and not w

for i in product((0,1),repeat=4):
    table =[
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            if [f(**(dict(zip(p,t)))) for t in table]  == [1,1,1]:
                print(*p, sep='')