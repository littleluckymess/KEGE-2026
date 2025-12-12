from itertools import permutations
cnt = 0
for val in set(permutations('ВОРОТА',  r=6)):
    val = ''.join(val)
    if 'ОА' not in val and 'ОО' not in val and 'АО' not in val:
        cnt += 1
print(cnt)
