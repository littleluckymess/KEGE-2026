for x in range(1, 2401):
    num = 7*9**210 + 6*9**110 - x
    cnt = 0
    while num:
        if num % 9 == 0:
            cnt += 1
        num //= 9
    if cnt == 100:
        print(x)