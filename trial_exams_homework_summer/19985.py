from itertools import permutations

matrix = '25 137 267 56 46 345 23'.split()
graph = 'АГ ГД ДЕ ЕВ ВБ БА АВ ДЖ ЖЕ'.split()

print(*range(1, 8))

for i in permutations('АБВГДЕЖ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)