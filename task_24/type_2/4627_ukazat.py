with open(r'../files/24_4627.txt') as file:
    data = file.readline()

ans = cnt = i = 0
while i < len(data) - 2:
    if data[i] + data[i + 1] + data[i + 2] in 'NPO PNO':
        cnt += 1
        i += 3
    else:
        ans = max(ans, cnt)
        cnt = 0
        i += 1
ans = max(ans, cnt)
print(ans)