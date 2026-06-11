ans = 0
for x in range(1, 4000):
    num = 9*13**9 + 5*13**5 + 2*13**2 - x
    cnt = 0
    while num:
        if num % 13 == 0:
            cnt += 1
        num //= 13
    if cnt % 2 == 0:
        ans += x
print(ans)
