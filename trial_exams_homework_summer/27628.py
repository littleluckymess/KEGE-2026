f = [0] * 2100

for n in range(2100):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = n * f[n - 1]
print((f[2024] - 5 * f[2023]) / f[2022])
