def f(start, end):
    if start == end: return 1
    return f(start + 10, end) + f(start - 5, end)
print()