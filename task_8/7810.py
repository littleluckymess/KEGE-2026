from itertools import product
cnt = 0
for val in product('МАСЛО',repeat=6):
    val = ''.join(val)
    if val.count('А') + val.count('О')== 1:
        cnt += 1
print(cnt)