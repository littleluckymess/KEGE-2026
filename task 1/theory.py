from itertools import permutations
matrix = 'все строки из матрицы'.split()
graph = 'все ребра из графа'.split()

print(*range(1, 8)) # количество столбцов в матрице
for i in permutations('названия вершин'):
    # for x, y in graph - извлекает рёбра из графа;
    # str(i.index(x) + 1) - сопоставляем вершину x с каким-то столбцом в перестановке i /
    # сопоставляем текущую перестановку i c матрицей;
    # matrix[i.index(y)] - сопоставляем вершину y с какой-то строкой в перестановке i;
    # str(i.index(x) + 1) in matrix[i.index(y)] - проверка, что столбец x пересекается со строкой y;
    # all() - проверяет, что все ребра существуют при текущей перестановке i;
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
       print(*i)