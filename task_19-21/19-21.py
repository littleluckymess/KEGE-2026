def f(x, y, s):
    if x + y > 40: return s % 2 == 0
    if s == 0: return False
    h = [
        f(max(x, y) + 1, min(x, y), s - 1),
        f(max(x, y) + 2, min(x, y), s - 1),
        f(max(x, y) + 3, min(x, y), s - 1)
    ]
    if x != y:
        h.append(f(max(x, y), min(x, y) * 2, s - 1))
    return any(h) if (s - 1) % 2 == 0 else all(h)

print('19)', min(x + y for x in range(1, 40) for y in range(1, 40) if f(x, y, 1)))
