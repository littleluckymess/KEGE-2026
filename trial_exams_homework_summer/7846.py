from itertools import combinations

def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = A1 <= x <= A2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))

line_A = [13, 17, 19, 23]
line_x = [14, 18, 20]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(max(ans))