from itertools import product
from string import printable as p

cnt = 0

for val in product(p[:14], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('9') == 1:
        for i in p[11:14]:
            val = val.replace(i, '*')
        if val.count('*') <= 3:
            cnt += 1
print(cnt)

