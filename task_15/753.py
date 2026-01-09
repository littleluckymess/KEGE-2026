from itertools import combinations

def f(x):
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    A = A1 <= x <= A2
    return (P == Q) <= (not A)
line = [x + eps for x in range(5,31) for eps in (0, 0.1, 0.9)]

ans = []

for A1, A2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))


