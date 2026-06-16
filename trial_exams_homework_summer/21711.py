f = [0] * 47_900

for n in range(47_900):
    if n < 20: f[n] = n
    if n >= 20: f[n] = (n - 6) * f[n - 7]

print((f[47_872] - 290 * f[47_865])/f[47_858])