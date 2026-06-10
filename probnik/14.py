for x in range(1, 2030):
    num = 6**260 + 6**160 + 6**60 - x
    cnt = 0
    while num:
        if num % 6 == 0:
            cnt += 1
        num //= 6
    if cnt == 202:
        print(x)