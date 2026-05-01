with open(r'../files/24_1975.txt') as file:
    data = file.readline()

cnt = 1
ans = []
for i in range(len(data) - 1):
    if data[i] + data[i + 1] != 'PP':
        cnt += 1
    else:
        ans += [cnt]
        cnt = 1

print(max(ans))

cnt = 1
ans = 0
for i in range(len(data) - 1):
    if data[i] + data[i + 1] != 'PP':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
    ans = max(ans, cnt)
print(ans)