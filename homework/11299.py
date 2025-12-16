from itertools import product
alph = sorted('БМЮРН')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 1 and val[0] != 'М' and val.count('Р') >= 2 and 'Ю'not in val:
        print(pos)

