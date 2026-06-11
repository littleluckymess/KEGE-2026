from itertools import*
from string import printable as p

cnt = 0
for val in product(p[:12], repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        for i in p[1:12:2]:
            val = val.replace(i, '*')
        if sum(i[0] == i[1] == '*'for i in zip(val, val[1:])) <= 2:
            cnt += 1
print(cnt)