f = [0] * 5000
g = [0] * 303_900

for n in range(304_000, 0, -1):
    if n > 303_728: g[n] = n - 15
    else: g[n] = g[n + 8]/2 - 109

for n in range(5000):
    if n >= 128: f[n] = f[n-5] + 1092
    else: f[n] = 5 * g[n - 7] + 29

print(f[2049])
