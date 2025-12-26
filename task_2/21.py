from itertools import product, permutations

def f(x,y,w,z):
    return not(y <= x) or (z <= w) or not z
for i in product((0,1), repeat=7):
    table = [
        (i[0], 0, i[1], i[2]),
        (0, 1, i[3], i[4]),
        (1, i[5], i[6], 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [0,0,0]:
                print(*p, sep='')
                

