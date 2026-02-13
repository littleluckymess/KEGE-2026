from fnmatch import fnmatch
from itertools import product
def not_prime(num):
    for i in range(2, int(num ** .5) +1):
        if num % i == 0:
            return True
    return False

all_N = []
for N in range(4, 10_000):
    if not_prime(N):
        all_N += [N]

ans = []
for N in all_N:
     num_mask = int(f'1{N}036')
     for i in range(num_mask - num_mask % 22768, 10**8 + 1, 22768):
         if fnmatch(str(i),'1N03*6*'):
             ans.append([i, N])
for i in sorted(ans):
    print(*i)

#####################################################################

ans =[]
for l1 in range(1, 5):
    for N in range(10**(l1 -1), 10**l1):
        if not_prime(N):
            for l2 in range(0, 4 -l1 + 1):
                for z1 in product('0123456789', repeat=l2):
                    z1 = ''.join(z1)
                    for l3 in range(0, 4 - l1 - l2 + 1):
                        for z2 in product('0123456789', repeat=l3):
                            z2 = ''.join(z2)
                            num = int(f'1{N}03{z1}6{z2}')
                            if num % 22768 == 0 and num < 10**8:
                                ans.append([num, N])
for i in sorted(ans):
    print(*i)




