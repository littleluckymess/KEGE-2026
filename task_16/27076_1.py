f = [0] * 2050
g = [0] * 12_000
q = [0] * 12_000

for n in range(12_000):
    if n < 21: q[n] = n + 4
    else: q[n] = q[n - 4] + 2

for n in range(12_000)[::-1]:
    if n < 11240: g[n] = g[n + 3] + 2
    else: g[n] = q[n]

for n in range(2050):
    if n < 43:
        f[n] = g[n + 4]
    else:
        f[n] = 2 * f[n - 2] - f[n - 4] + 2

print(f[2026])
