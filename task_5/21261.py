def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

# ans_R = []
# ans_N = []
ans = []
for N in range(1, 100_000):
    R = convert(N, 4)
    if sum(map(int,R)) % 3 == 0:
        R = R.replace('0','*')
        R = R.replace('2','*')
        R = R.replace('*','2')
        R += '32' + R
    else:
        R = R[0] + '10' + R[3:] + '33'
    R = int(R,4)
    if R > 320:
        ans.append([R,N])
print(max(ans))



#     if R > 320:
#         ans_R.append(R)
#         ans_N.append(N)
#
# min_R = min(ans_R)
# for i in range(len(ans_N)):
#     if ans_R[i] == min_R:
#         print(ans_N[i])
