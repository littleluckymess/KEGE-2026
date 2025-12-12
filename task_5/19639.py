ans = []
for N in range(1,100_000):
    R = bin(N)[2:]
    if R.count('0') % 2 == 0:
        R = '1' + R + '1'
    else:
        R = '10' + R
    R = int(R,2)
    if R < 100:
        ans.append(R)
print(max(ans))
