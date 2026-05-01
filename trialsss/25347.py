from itertools import product

for pos, val in enumerate(product(sorted('ГРАНИТ'), repeat=6), start=1):
    val = ''.join(val)
    if val[0] not in 'АИГ'and val.count('А') == 1:
        pos += 1
        if pos % 2 == 1:
            print(pos, val)
            break