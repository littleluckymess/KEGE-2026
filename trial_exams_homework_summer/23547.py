from itertools import permutations

matrix = '24 134 267 125 47 37 356'.split()
graph = 'GA AF FC CD DB BE EG GF BC'.split()

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)