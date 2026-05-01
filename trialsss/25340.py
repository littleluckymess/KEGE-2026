from itertools import permutations

graph = 'BH HD DA AC CB HF FE EG GC GA'.split()
matrix = '368 34 126 27 67 135 458 17'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)



