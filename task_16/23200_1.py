f = [0] * 6300

for n in range(6300):
    if n < 10: f[n] = n
    else: f[n] = 3*n + f[n - 3]

print((f[6250] + 2*f[6244]) // f[6238])