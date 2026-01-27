from fnmatch import fnmatch
for N in range(12347 - 12347 % 141, 10**8 + 1, 141):
    if fnmatch(str(N), '1234*7'):
        print(N, N//141)

####################################################

from itertools import product
from string import printable
ans = []
for L in range(0,4):
    for Z in product(printable[:10], repeat=L):
        num = int('1234' + ''.join(Z) + '7')
        if num % 141 == 0 and num <= 10**8:
            ans.append([num, num//141])
for i in sorted(ans):
    print(*i)

