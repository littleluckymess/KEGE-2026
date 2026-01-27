from itertools import permutations
from string import printable as p
cnt=0
for val in permutations(p[2:8], r=5):
    val = ''.join(val)
    if val[0] != '0':
        print(val)
        for i in '357':
            val = val.replace(i,'*')
        for i in '46':
            val = val.replace(i,'+')
    if '**' not in val and '++' not in val:
        cnt += 1
print(cnt)
