def convert(num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(0,100_000):
    R = convert(N,4)
    if N % 2 == 0:
        R = '12' + R + convert(int(R[-1]) * 3,4)
    else:
        R = '13' + R + '21'
    R = int(R,4)
    if R > 50:
        ans.append(R)
print(min(ans))


