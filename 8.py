from itertools import product, permutations

words = []
for val in permutations('КОТЕНОК'):
    val = ''.join(val)
    words.append(val)

for pos, val in enumerate(product(sorted('КОТЕНА'), repeat=7), start=1):
    val = ''.join(val)
    if val in words and pos % 2 != 0:
        print(pos)



