from itertools import product
from string import printable as p

cnt = 0
for val in product(p[:7], repeat=5):
    val = ''.join(val)
    if '0' not in val[0]:
        for i in val:
            val = val.replace('0246', '*')
            for x in val:
                val = val.replace('012', '+')
                if '*' in val[0] and '+' not in val[-1] and val.count('4') <= 1:
                    cnt += 1
print(cnt)