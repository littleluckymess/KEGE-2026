from itertools import permutations

cnt = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    summ = 0
    for i in range(len(val)):
        if val[i] in 'АИ':
            summ += i + 1
    if summ == 11:
        cnt += 1

print(cnt)

