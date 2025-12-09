
from itertools import product
alph = sorted('СОЛНЦЕ')
cnt = 0
for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] not in 'ОЕ' and val.count('Ц') == 2:
        cnt +=1
print(cnt)
