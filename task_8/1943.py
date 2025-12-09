
from itertools import product
cnt = 0
for val in product('ЗЕРКАЛО', repeat=6):
    val = ''.join(val)
    if 1 <= val.count('К') <= 4:
        val = val.replace('К', '')
        if len(val) == len(set(val)):
            cnt += 1
print(cnt)