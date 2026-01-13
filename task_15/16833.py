from itertools import combinations
def f(x):
    P = 25 <= x <= 73
    Q = 75 <= x <= 118
    A = A1 <= x <= A2
    return (A and (not Q)) <= (P or Q)

line_A = [25, 73, 75, 118]
line_x = [31, 74, 89]

ans =[]
for A1, A2 in combinations(line_A,2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(max(ans))