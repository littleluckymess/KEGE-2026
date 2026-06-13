from itertools import product
from string import printable as p

cnt = 0

for val in product(p[:9], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') == 1:
        for i in p[1:9:2]:
            val = val.replace(i, '*')
        if '*0' not in val and '0*' not in val:
                cnt += 1
print(cnt)