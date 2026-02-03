from fnmatch import fnmatch
for N in range(30120145 - 30120145%1917, 10**10 + 1, 1917):
    if fnmatch(str(N), '3?12?14*5'):
        print(N, N//1917)