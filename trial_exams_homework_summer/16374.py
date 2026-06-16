from itertools import product
from string import printable as p

cnt = 0
for val in product(p[:7], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in p[:7:2]:
            val = val.replace(i, '*')
        if val.count('*') == 2:
            cnt += 1
print(cnt)