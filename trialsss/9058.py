ans = []
for N in range(1, 100_000):
    R = f'{N:b}'
    if N % 2 == 0:
        R = '1' + R + str(sum(map(int, R)) % 2)
    else:
        R = R + '0' + str(sum(map(int, R)) % 2)
    R = int(R, 2)
    if R > 100:
        ans.append([R, N])
print(min(ans))
