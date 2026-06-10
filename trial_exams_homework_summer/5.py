ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    D = sum(map(int, R))
    if D % 2 == 0:
        R = '10'+ R[2:] + '1'
    else:
        R = '11' + R[2:] + '0'
    R = int(R, 2)
    if N < 16:
        ans.append(R)
print(max(ans))
        