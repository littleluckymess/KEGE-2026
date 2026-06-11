from itertools import*
from string import printable as p

cnt = 0
for val in product(p[:5], repeat=9):
    val = ''.join(val)
    if val[0] != '0':
        for i in '024':
            val = val.replace(i, '*')
        if val.count('**') == 2 and '***' not in val:
            cnt += 1
print(cnt)