from itertools import combinations

def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = A1 <= x <= A2
    return (B <= A) and ((not C) or A)

line = [x + eps for x in range(16,53) for eps in (0, 0.1, 0.9)]

ans = []
for A1, A2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(min(ans))

