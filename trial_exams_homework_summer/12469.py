from itertools import combinations

def f(x):
    D = 7 <= x <= 68
    C = 29 <=x <= 100
    A = A1 <=x <= A2
    return D <= (((not C) and (not A)) <= (not D))

line_A = [7, 29, 68, 100]
line_x = [8, 29, 69]
ans = []

for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(min(ans))