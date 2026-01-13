from itertools import combinations


def f(x):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not (C or J)) <= (not A)

line = []

line_A=[48, 83, 94, 100]
line_x=[60, 91, 97]

ans = []
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 -A1)

print(max(ans))