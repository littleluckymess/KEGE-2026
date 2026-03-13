from itertools import permutations

graf = 'AF FE EC CG GD DB BA FB ED'.split()
matrix ='256 134 267 27 16 135 34'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graf):
        print(*i)

