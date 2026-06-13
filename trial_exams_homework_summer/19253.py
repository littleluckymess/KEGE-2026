def f(start, end):
    if start == end: return 1
    if start < end or start == 24: return 0
    return f(start - 1, end) + f(start - 6, end) + f(start // 2, end)

print(f(34, 29) * f(29,19) * f(19, 6))