from fnmatch import fnmatch
for N in range(1021394 - 1021394 % 2023, 10**10 + 1, 2023):
    if fnmatch(str(N),'1?2139*4'):
        print(N, N//2023)