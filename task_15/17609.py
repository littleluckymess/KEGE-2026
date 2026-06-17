def f(x):
    return (x % 33 == 0) <= ((x % A != 0) <= (x % 242 != 0))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break