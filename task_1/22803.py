from itertools import permutations

graph = 'GE EF FA AB BG EC FD AD BC DC'.split()
matrix = '457 567 45 146 123 247 126'.split()

print(*range(1,8))

for i in permutations('ABCDEFG'):
    if all (str(i.index(x) + 1) in matrix[i.index(y)] for x,y in graph):
        print(*i)
