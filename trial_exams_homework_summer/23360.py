from itertools import permutations

matrix = '345 67 14 123567 147 24 245'.split()
graph = 'AF FE ED DC CB BG CG DG EG FG AG'.split()

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)