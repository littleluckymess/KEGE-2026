from itertools import product

for pos, val in enumerate (product(sorted('АПРЕЛЬ'),repeat=6), start = 1):
    val = ''.join(val)
    if val[0] not in 'АЛ' and val.count('П') >= 2:
        if pos % 2 == 1 :
            print(pos, val)
            break
