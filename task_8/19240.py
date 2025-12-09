
from itertools import product
alph = sorted('ЯНВАРЬ')
cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('Ь')<=1 and 'ЯЯ' not in val and val[0] and 'Я' not in val[0]:
        print(pos)