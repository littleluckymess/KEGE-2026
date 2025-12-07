from itertools import*
cnt=0
for val in product('ПСКАЛЬ', repeat=4):
    val=''.join(val)
    if val[0]!='Ь' and 'ЬЬ' not in val:
        cnt+=1
print(cnt)