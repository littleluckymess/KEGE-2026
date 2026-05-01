f = [0] * 250_000
g = [0] * 250_000

for n in range(250_000)[::-1]:
    if n >= 248_045: g[n] = n / 20 + 28
    else: g[n] = g[n + 9] - 4

for n in range(250_000):
    if n >= 19: f[n] = f[n - 4] + 3580
    else: f[n] = 6 * (g[n - 7] - 36)

print(f[673])

