from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10**8, 141):
    if fnmatch(str(N), '1234*7'):
        print(N, N // 141)