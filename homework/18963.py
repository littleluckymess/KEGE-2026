from itertools import product
cnt = 0
alph = 'КОТБУС'
for val in product(alph, repeat = 8):
    val =''.join(val)
    if val[0] not in 'ОУ' and 'КОТ' in val:
        cnt += 1
print(cnt)