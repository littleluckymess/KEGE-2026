# print ('x y w z')
# for x in 0,1:
#     for y in 0,1:
#         for w in 0,1:
#             for z in 0,1:
#                 f = not(x <= y) or ( z == w) or z
#                 if not f:
#                     print(x, y, w, z)

from itertools import product, permutations
def f(x,y,w,z):
    return not(x <= y) or (z == w) or z
for i in product((0,1), repeat=6):

