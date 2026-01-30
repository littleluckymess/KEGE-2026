from itertools import product
alph = sorted('АЕКНС')
for pos, val in enumerate(product(alph, repeat=6),1):
    val = ''.join(val)
    if val == 'СЕНЕКА':
        print(pos)






