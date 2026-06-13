from fnmatch import fnmatch

for N in range(161, 10**8, 161):
    if fnmatch(str(N), '12*4?65'):
        print(N, N//161)