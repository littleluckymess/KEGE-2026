from itertools import product, permutations

alph = sorted('ЦИТРУС')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('И') == 2 and 'ЦЦ' not in val:
        print(pos)