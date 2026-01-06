from itertools import product, permutations
def f(x,y,w,z):
    return (z <= y) or ((w <= x) <= y)
for i in product((0,1), repeat=6):
    table = [(i[0],0, 0, i[1]),
             (i[2], i[3],1, i[4]),
             (i[5], 1, 1, 1)]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [0,0,0]:
                print(*p, sep='')