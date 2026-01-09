from itertools import product
from string import printable as alph
cnt=0
for val in product(alph[:14],repeat=5):
    val = ''.join(val)
    if val[0] != '0' and (val[-1] == '0' or val[-1] == '3'):
        if len(set(val)) == 2:
            cnt+=1
print(cnt)

