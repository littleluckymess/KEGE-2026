from itertools import*
cnt=0
for val in product('ГЕПАРД', repeat=5):
    val=''.join(val)
    if val[0]!='А' and val[-1]!='Е' and  val.count('Г')==1:
        cnt+=1
print(cnt)