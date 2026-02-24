def f(start, end):
    if start == end: return 1
    if start > end: return 0
    return f(start + 2, end) + f(start + 5, end) + f(start**2, end)

print(f(4, 36) - 1)

##############################

def f(start, end):
    if start == end: return 1
    if start > end: return 0
    if start == 6:
        return  f(start + 2, end) + f(start + 5, end)
    return f(start + 2, end) + f(start + 5, end) + f(start**2, end)

print(f(4, 36))

###########################

def f(start, end, last):
    if start == end and last != 'C': return 1
    if start > end: return 0
    return f(start + 2, end, 'A') + f(start + 5, end,'B') + f(start**2, end, 'C')

print(f(4, 36,''))
