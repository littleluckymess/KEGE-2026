def count_0(num, sys):
    count = 0
    while num:
        if num % sys == 0:
            count += 1
        num //= sys
    return count

for x in range(1, 27_000):
    num = 3*27**9 + 2*27**6 + 27**3 - x
    if count_0(num,27) == 6:
        print(x)
        break


