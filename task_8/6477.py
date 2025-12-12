from itertools import permutations
cnt = 0
for val in set(permutations('ЛЕВИОСА')):
    val = ''.join(val)
    if val[0] != 'ЕИОА' and val[(len(val))//2] not in 'ЛВС':
        cnt += 1
print(cnt)