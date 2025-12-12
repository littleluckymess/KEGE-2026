from itertools import product

alph = sorted('СУБЛИМАЦЯ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 1 and val[-1] != 'Я':
        for i in 'УИАЯ':
            val = val.replace(i, '*')
        if val.count('*') == 2:
            print(pos)