from fnmatch import fnmatch

for N in range(10101011- 10101011 % 2023, 10**10 + 1, 2023):
     if fnmatch(str(N), '1?1?1?1*1'):
         if sum(map(int, str(N))) == 22:
            print(N)
