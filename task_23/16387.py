def f(start, end):
    if start == end: return 1
    if start > end or start == 16: return 0
    return f(start + 1, end) + f(start + 2,end) + f(start * 3, end)
print(f(2, 9) * f(9,18))