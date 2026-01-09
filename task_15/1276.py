from itertools import combinations

def f(x):
    P = 15 <= x <= 33
    Q = 35 <= x <= 48
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

line = [x + eps for x in range (15, 49) for eps in (0, 0.1, 0.9)]

ans = []
for A1, A2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))
