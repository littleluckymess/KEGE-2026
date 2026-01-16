cnt = 0
num = 17*125**453 + 117*5**231 - 3*5**13 - 2357
while num:
    if num:
        num = num % 125 <= 37
num//=125
cnt += 1
print(cnt)


