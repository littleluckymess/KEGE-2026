def f(start, end):
    if start == end: return 1
    if start < end or start == 24: return 0
    return f(start - 1, end) + f(start - 4, end) + f(start // 2, end)

print(f(34, 30) * f(30, 20) * f(20, 9))