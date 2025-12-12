from itertools import product
from string import printable as p
cnt = 0
for val in product(p[:16],repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 1 and val[0] != val[1]  != val[2] != val[3]:
        cnt += 1
print(cnt)
