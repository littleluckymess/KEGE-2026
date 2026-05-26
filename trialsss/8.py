from itertools import product as pro
from string import printable as pri

cnt = 0
for i in pro(pri[:13], repeat=6):
    i = ''.join(i)
    if i[0] != '0':
        u1 = i.count('0') > 1
        for t in pri[10:13]:
            i = i.replace(t, '*')
        u2 = '**' in i
        u3 = i.count('*') == 2
        if all((u1, u2, u3)):
            cnt += 1
print(cnt)