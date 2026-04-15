from itertools import product
from string import printable as p

cnt = 0

for val in product(p[:7], repeat=7):
    val = ''.join(val)
    if val[0]  not in '035':
        u1 = '22' in val
        u2 = '44' in val
        if u1 + u2 < 2:
            cnt += 1
print(cnt)




