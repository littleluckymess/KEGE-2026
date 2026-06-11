f = [0] * 6500

for n in range(6500):
    if n < 10:
        f[n] = n
    if n >= 10:
        f[n] = 3*n +f[n - 3]
print((f[6250] + 2*f[6244]) / f[6238])