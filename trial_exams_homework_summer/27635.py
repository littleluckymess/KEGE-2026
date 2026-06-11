from fnmatch import fnmatch

for N in range(1230056 - 1230056 % 171, 10**8 + 1, 171):
    if fnmatch(str(N), '1*23??56'):
        print(N, N // 171)
