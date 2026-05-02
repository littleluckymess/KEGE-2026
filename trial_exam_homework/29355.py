from fnmatch import fnmatch

for N in range(89607090 - 89607090 % 9874, 10**10, 9874):
    if fnmatch(str(N), '89*6?7?9?'):
        print(N, N//9874)