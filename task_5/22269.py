
def convert(num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = convert(N,5)
    if R[-1] == '0':
        R = R.replace('1','*')
        R = R.replace('4','1')
        R = R.replace('*','4')
        R = '33' + R
    else:
        R = '3' + R[1:] +'42'
    R = int(R,5)

    if R < 1922:
        ans.append([R,N])

max_R = max(ans)[0]
all_N = []
for R,N in ans:
    if R == max_R:
        all_N.append(N)
print(min(all_N))


