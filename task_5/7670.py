ans = []
for N in range(151,100_100):
    R = hex(N)[2:]
    R = R.replace('a','1')
    cnt = 0
    for i in R:
        if int(i,16) % 2 == 0:
            cnt += 1
    if R.count('1') % 2 == 0 > 2:
            R = R + 'B'
    else:
            R = 'F' + R
    R = int(R,16)
    if R > 3500:
        ans.append([R, N])
print(min(ans))


