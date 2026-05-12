def f(start, end):
    if start == end: return 1
    if start < end or start == 73: return 0
    return f(start - 3, end) + f(start - 8, end) + f(start //2, end)
print(f(76, 41) * f(41, 12))