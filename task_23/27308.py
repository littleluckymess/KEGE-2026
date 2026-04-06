
def f(start, end):
    if start == end: return 1
    if start < end: return 0
    return f(start - 3, end) + f(start - 5, end) + f(start // 3, end)

a1 = f(80,18)*f(18, 3)
a2 = f(80, 38)*f(38,3)
a3 = f(80,38) * f(38, 18) * f(18,3)
print(a1 + a2 - a3)
