from itertools import*

for pos, val in enumerate(product(sorted('ПОЛЕНИЦА'), repeat=5), start=1):
    val = ''.join(val)
    if 'А' not in val[0] and 'А' not in val[-1] and val.count('Л') >= 3:
        if pos % 2 == 1:
            print(pos)
            break