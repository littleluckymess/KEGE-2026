
from string import printable

def convert (num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num10= 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
num27 = convert(num10, 27)

cnt1=0
for i in num27:
    if int(i,27) > 9:
        cnt1 += 1
print(cnt1)

##
cnt2=0
for i in printable[10:27]:
    if int(i,27) > 9:
        cnt2 += num27.count(i)
print(cnt2)

###
cnt3=0
for i in num27:
        if i in printable[10:27]:
            cnt3 += 1
print(cnt3)
