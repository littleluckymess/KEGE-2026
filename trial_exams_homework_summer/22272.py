def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 100_000):
    R = convert(N, 9)
    if R[0] == '7':
        R = R.replace('6','3')
        R = R.replace('*', '3')
        R = R.replace('3', '6')
        R = '34' + R
    else:
        R = '3' + R[1:] + '45'
    R = int(R, 9)
    if R < 2876:
        ans.append([N, R])
print(max(ans))
