from itertools import product

for pos, val in enumerate(product(sorted('СИМВОЛ'),repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'ОС' and val.count('В') == 1 and val.count('С') <= 1:
        if pos % 2 == 1:
            print(pos, val)


