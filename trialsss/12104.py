from itertools import combinations

def f(x):
    P = 56 <= x <= 79
    Q = 63 <= x <= 85
    A = A1 <= x <= A2
    return (not (P <= Q))<= ((not Q) <= A)
line_A = [56, 63, 79, 85]
line_x = [57, 64, 80, 86]

ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(min(ans))

