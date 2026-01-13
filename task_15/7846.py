from itertools import combinations

def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = A1 <= x <= A2
    return (not((not(P)) <= Q)) <= (A <= ((not(Q)) <= P))

line = [x + eps for x in range(12,24) for eps in (0, 0.1, 0.9)]

ans = []
for A1, A2 in combinations(line,2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)
print(max(ans))

