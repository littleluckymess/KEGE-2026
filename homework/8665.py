from itertools import product
from string import printable as p
cnt=0
for val in product(p[:12], repeat=7):
    val = ''.join(val)
    if val[0] != 0 and val.count('B') == 2:
        cnt += 1
print(cnt)

