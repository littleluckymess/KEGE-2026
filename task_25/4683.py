from fnmatch import fnmatch
for N in range(2123406 - 2123406 % 37, 10**8 + 1, 37):
    if fnmatch(str(N), '2*1234?6'):
        print(N, N//37)