from itertools import permutations

matrix = '248 157 456 136 23 34 28 17'.split()
graph = 'FC CH HB BE EA AF CG GD DH AB'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)