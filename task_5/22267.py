def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N,7)
    if R[-1:] == '2':
        R = R.replace('3', '*')
        R = R.replace('1','3')
        R = R.replace('*', '1')
        R = '21' + R
    else:
        R = '1' + R[1:] + '36'
    R = int(R,7)
    if R < 744:
        ans.append([R,N])
print(max(ans))