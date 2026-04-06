
f = [0] * 3010
for n in range(3001):
    if n == 1: f[n] = 1
    if n > 1: f[n] = n * f[n - 1]
print((2 * f[2024] + f[2023])/f[2022])