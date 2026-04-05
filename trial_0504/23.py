def f(start, end):
    if start == end: return 1
    if start < end or start == 7: return 0
    return f(start - 1, end) + f(start - 4, end) + f(start // 3, end)

print(f(19, 13) * f(13, 2))