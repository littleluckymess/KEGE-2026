def f(x, s):
    if x >= 16: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x - 3, s - 1)
        + f(x - 8, s - 1)
        + f(x // 3, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [x for x in range(16, 1) if f(x, 2)])
print('20)', [x for x in range(16, 1) if f(x, 3) and not f(x, 1)])
print('21)', [x for x in range(16, 1) if f(x, 4) and not f(x, 2)])