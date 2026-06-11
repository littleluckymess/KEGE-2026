from itertools import product
from string import printable as p
cnt = 0
for val in product(p[:7], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1 and '00' not in val and '11' not in val and '22' not in val and '33' not in val and '44' not in val and '55' not in val and '66' not in val and '77' not in val:
        if sum(i + i in val for i in '0123456') == 0:
           cnt += 1
print(cnt)