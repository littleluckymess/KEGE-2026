def f(x, s):
    if x <= 13: return s % 2 == 0
    if s == 0: return False
    h = [f(x - 2, s - 1),
         f(x // 1.5, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)
print('19)', [x for x in range(14, 100) if f(x,2)])
print('20)', [x for x in range(14, 100) if f(x,3)  and not f(x, 1)])
print('21)', [x for x in range(14, 100) if f(x,4)  and not f(x, 2)])
