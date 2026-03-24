def f(x):
    return (a % 25 == 0) and (((x % 24 == 0) and (x % 75 == 0)) <= (x % a == 0))
cnt = 0
for a in range(-1000, 1000):
    if a and all(f(x) for x in range(-1000, 1000)):
        cnt += 1
print(cnt)