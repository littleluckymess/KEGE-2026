def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num//=sys
    return res [::-1] if res else '0'
ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + str(convert(sum(map(int, R)) * 2, 3))
    R =int(R, 3)
    if R % 2 == 1 and R > 502:
        ans.append(R)
print(min(ans))