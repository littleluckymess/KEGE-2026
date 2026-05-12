f = [0] * 300_000
g = [0]* 300_000

for n in range(1, 300_000)[::-1]:
    if n >= 22_560: g[n] = n / 23 + 33
    else: g[n] = g[n + 11] - 4

for n in range(1, 300_000):
    if n >= 21: f[n] = f[n - 8] + 1095
    else: f[n] = 10 * (g[n - 7] - 36)

print(f[548])