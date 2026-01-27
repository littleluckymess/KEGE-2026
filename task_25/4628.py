from fnmatch import fnmatch
for N in range(124065 - 124065 % 161, 10**8 + 1, 161):
    if fnmatch(str(N),'124*?65'):
        print(N, N//161)

from itertools import product
from string import printable

#100000000
#12*4?65
ans = []
for V in printable[:10]:
    for L in range(0,3):
        for Z in product(printable[:10], repeat=L):
            num = int(f'12{''.join(Z)}4{V}65')
            if num % 161 == 0 and num < 10**8:
                ans.append([num, num//161])

for i in sorted(ans):
    print(*i)




