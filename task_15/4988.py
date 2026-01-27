cnt = 0
def f(x):
    return (x % 12 == 0) and (70 <= x <= 80) and (not(x % A == 0))

for A in range(1,1000):
    if all(not f(x) for x in range(1,1000)):
        cnt += 1
print(cnt)