k = 0
for N in range(1,100_100):
    R = hex(N)[:2]
    if R.count('B') % 2 == 0:
        R = '1' + R
    else:
        R = R + '1'
    R = int(R,16)
    if len(str(R)) == 2:
        k += 1
print(k)


