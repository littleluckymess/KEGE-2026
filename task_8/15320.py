from itertools import product
for pos, val in enumerate(product(sorted('ПАРУС'), repeat=5), start=1):
    val=''.join(val)
    if val.count('У')<=1 and 'АА' not in val:
                print(pos,val)
                break

