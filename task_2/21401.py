
from itertools import product, permutations
def f (x,y,w,z):
    return x and (z <= w) and not y
for i in product((0,1), repeat=7):
    table = [(i[0], i[1], 1, i[2]),
             (i[3], 1, 0, i[4]),
             (1, 0, i[5], i[6])]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p,sep='')
