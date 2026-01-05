from itertools import product
from string import printable as p
cnt = 0
for val in product(p[:9], repeat=7):
    val = ''.join(val)
    if val[0] not in '013579' and val[-1] not in '0369' and '6' in val:
        cnt += 1
print(cnt)
