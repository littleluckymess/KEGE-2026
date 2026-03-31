from itertools import product
from string import printable

cnt = 0

for val in product(printable[:25], repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        for i in printable[:16:2]:
            val = val.replace(i, '*')
        for i in printable[16:25:2]:
            val = val.replace(i, '+')
        for i in printable[16:25]:
            val = val.replace(i, '#')
        if val.count('*') + val.count('+') >= 1 and val.count('#') + val.count('+') > 2:
            cnt += 1

print(cnt)