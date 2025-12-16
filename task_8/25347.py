from itertools import product
alph = sorted('ГРАНИТ')
for pos,val in enumerate(product(alph,repeat=6),start=1):
    if pos % 2 == 1 and val[0] not in 'АИГ'and val.count('А') == 1:
        print(pos)
