from itertools import product,permutations

def f(m,e,o,w):
    return (m <= e) or (o == e) and w

for i in product((0,1), repeat = 4):
    table = [
        (1, 0, 1, 1),
        (1, i[0], i[1], i[2]),
        (0, i[3], 1, 0)
    ]
    if len(set(table)) == len(table):
        for p in permutations('meow'):
            if [f(**dict(zip(p,t))) for t in table] == [0, 0, 0]:
                print(*p, sep='')