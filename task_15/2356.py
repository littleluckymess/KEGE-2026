from itertools import combinations

def f(x):
    P =  10 <= x <= 45
    Q = 35 <= x <= 78
    A = A1 <= x <= A2
    return ((not P) <= Q) and not A

line = [x + eps for x in range(10,79) for eps in (0, 0.1, 0.9)]

ans = []
for A1, A2 in combinations(line, 2):
    if all(not f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))



