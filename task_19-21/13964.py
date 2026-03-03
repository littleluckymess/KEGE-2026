def f(x, y, s):
    if x + y <= 108: return s % 2 == 0
    if s == 0 : return False
    h = [f(x - 2, y, s - 1),
         f(x, y - 2, s - 1)]
    if x % 2 == 0:
        h += [f(x // 2, y, s - 1)]
    else:
        h += [f(x // 2 + 1, y, s - 1)]
    if y % 2 == 0:
        h += [f(x, y // 2, s - 1)]
    else:
        h += [f(x , y // 2 + 1, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', [x for x in range(48, 1000) if f(x, 60, 2)])
print('20)', [x for x in range(48, 1000) if f(x, 60, 3) and not f(x, 60, 1)])
print('21)', [x for x in range(48, 1000) if f(x, 60, 4) and not f(x, 60, 2)])
