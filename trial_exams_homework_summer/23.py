def f(start, end):
    if start == end: return 1
    if start > end or start == 10: return 0
    return f(start + 1, end) + f(start + 2, end) + f(start * 2, end)

print(f(3, 7) * f(7, 20))