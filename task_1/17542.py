from itertools import permutations
graph = 'DE EA AH HC CF FG GB BD BE GH'.split()
matrix = '38 58 146 36 27 347 568 127'.split()

print(*range(1,9))
for i in permutations('ABCDEFGH'):
     if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
         print(*i)
