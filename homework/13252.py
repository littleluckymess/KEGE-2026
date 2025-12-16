from itertools import permutations
alhp ='КИДАЛА'
cnt = 0
for val in set(permutations(alhp, r=5)):
    val = ''.join(val)
    if 'КК' not in val and 'ИИ' not in val and 'ДД' not in val and 'АА' not in val and 'ЛЛ' not in val:
        cnt += 1
print(cnt)