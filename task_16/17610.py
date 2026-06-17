f = [0] * 2100

for n in range(1, 2100):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = (n + 1) * f[n - 1]

print((f[2024] + 3*f[2023]) / f[2022])