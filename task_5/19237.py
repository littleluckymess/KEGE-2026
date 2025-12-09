def convert (num,sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range (1, 100_000):
    R = convert(N,3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + (convert(sum(map(int,R)),3))

    R = int(R,3)
    if R > 220 and R % 2 == 0:
        ans.append(R)
print(min(ans))
