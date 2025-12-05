from itertools import product
cnt = 0
for val in product('ГЕПАРД', repeat=5):
    val = ''.join(val)
    if val.count('Г') == 1 and val[0] not in 'А' and val[-1] != 'Е':
        cnt += 1
print(cnt)