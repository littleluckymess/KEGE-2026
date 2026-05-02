def f(x, y, s):
    if x + y >= 154: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x + 4, y, s - 1),
        f(x * 3, y,s - 1),
        f(x, y + 4, s - 1),
        f(x, y * 3, s - 1)
    ]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [s for s in range(1, 142) if f(s, 11, 2)])
print('20)', [s for s in range(1, 142) if f(s, 11, 3) and not f(s, 11, 1)])
print('21)', [s for s in range(1, 142) if f(s, 11, 4) and not f(s, 11, 2)])
