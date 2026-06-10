f = [0] * 43_000
g =[0] * 43_000

for n in range(43_000):
    if n > 9:
        g[n] = g[n-4] + 2
    if n <= 9:
        g[n] = 3 * n

for n in range(43_000):
    f[n] = g[n - 1] + g[n - 3]

print(f[42_999])
