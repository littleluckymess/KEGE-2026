f = [0] * 2200

for n in range(2200):
    if n <= 5: f[n] = 1
    else: f[n] = n + f[n - 2]

print(f[2126] - f[2122])