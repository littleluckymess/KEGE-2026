from itertools import product, repeat

for pos, val in enumerate(product(sorted('ЛАЙМ'),repeat=5),start=1):
    val = ''.join(val)
    if 'Л' not in val and 'М' not in val and 'ЙЙ' not in val:
        print(pos)