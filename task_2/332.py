from itertools import permutations
def f (x,y,w,z):
    return (x or y and (not z)) and (not w)
table = [(1, 0, 0, 0),
         (0, 0, 1, 0),
         (0, 1, 0, 1)]
for p in permutations('xywz'):
        if [f(**dict(zip(p,t))) for t in table] == [1, 1, 0]:
            print(*p, sep='')
