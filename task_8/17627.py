from itertools import product
from string import printable as p

cnt=0
for val in product(p[:15],repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        if len([i for i in val  if int(i,15) > 9]) >= 2:
            if [1 for i in val  if int(i,15) > 9].count(1) >= 2:
                if sum ([1 for i in val if int(i, 15) > 9]) >= 2:
                    if sum([val.count(i) for i in p[10:15]]) >= 2:
                        cnt += 1
print(cnt)





