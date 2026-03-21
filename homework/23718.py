from itertools import permutations

matrix = '25 159 78 67 126 457 346 39 28'.split()
graph = 'КО ОТ ТЛ ЛЕ ЕВ ВУ УЯ ЯМ МК КТ ЛВ '.split()

print(*range(1,10))

for i in permutations('КОТЛЕВМЯУ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
