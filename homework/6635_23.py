def f(start, cnt=0):
    if cnt == 13:
        if start < 0:
            return {start}
        return set()
    return f(start - 3, cnt + 1) | f(start * (-3), cnt + 1)

ans = f(333)
print(len(ans))
