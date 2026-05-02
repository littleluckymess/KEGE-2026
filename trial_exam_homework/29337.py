ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    if sum(map(int,R)) % 2  == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    if R <= 19:
        ans.append(N)
print(max(ans))