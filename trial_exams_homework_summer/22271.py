def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num//= sys
    return res[::-1] if res else '0'

ans =[]
for N in range(1, 100_000):
    R = convert(N, 8)
    if R[0] == '5':
        R = R.replace('2', '1')
        R = R.replace('1', '*')
        R = R.replace('*', '2')
        R = '11' + R
    else:
        R = '2' + R[1:] + '10'
    R = int(R, 8)
    if R < 1354:
        ans.append([N, R])
print(max(ans))