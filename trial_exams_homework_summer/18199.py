def f(x, y, s):
    if x + y >= 77: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x + 3, y, s - 1),
        f(x, y + 3, s - 1),
        f(x * 3, y, s - 1),
        f(x, y * 3, s - 1)

    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19', [s for s in range(1, 64) if f(s,12, 2)])
print('20', [s for s in range(1, 64) if f(s,12, 3) and not f(12,s, 1)])
print('21', [s for s in range(1, 64) if f(s,12, 4) and not f(12,s, 2)])