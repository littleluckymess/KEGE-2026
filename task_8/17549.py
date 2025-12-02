from itertools import product
alph = sorted('ФОКУС')
for pos, val in enumerate(product(alph,repeat=5), start = 1):
    val = ''.join(val)
    if 'Ф' not in val and val.count('У') == 2:
        print(pos)


