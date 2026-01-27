
for x in range(1,2006):
    num = 4**163 * 5 + 12**62 - x
    cnt_1 = 0
    cnt_4 = 0
    while num:
        if num % 5 == 1:
            cnt_1 += 1
        elif num % 5 == 4:
                cnt_4 += 1
        num //= 5
    if cnt_1 < cnt_4:
        print(x)




