# print ('x y w z')
# for x in 0,1:
#     for y in 0,1:
#         for w in 0,1:
#             for z in 0,1:
#                 f = not (w <= (x == (y or y))) and (z <= x)
#                 if f:
#                     print(x, y, w, z, f)

from itertools import product, permutations
def f(x, y, w, z):
    return not (w <= (x == (y or y))) and (z <= x)
for i in product((0,1), repeat = 5):
    table = [
        (i[0], 1, 1, i[1]),
        (0, i[2], i[3], 0),
        (i[4], 0, 1, 0)

    ]
    if len(set(table)) == len(table):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]:
                print(*p,sep='')
