from itertools import permutations
from string import printable as p

cnt = 0

for val in permutations(p[:7], r=7):
    val = ''.join(val)
    if '0' not in val[0]:
        if val[0] != '35' and val[0] != '53':
            if '22' and '44' not in val:
                cnt += 1
    print(cnt, val)




