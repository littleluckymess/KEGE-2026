ans =[]
for N in range(1,100_000):
    R = bin(N)[2:]
    R = R.replace('0','00')
    R = R.replace('1','11')
    R = int(R,2)
    if R > 63:
        ans.append(R)
print(min(ans))


