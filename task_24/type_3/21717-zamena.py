with open(r'../files/24_21717.txt') as file:
    data = file.readline()

data = data.replace('RSQ', 'Rsq rsQ')
data = data.split()

ans = 10 ** 10
for i in range(len(data) - 128 - 1):
    line = ''.join(data[i:i+129]).replace('sqrs', 'S')
    for j in data[i+129][3:]:
        line += j
        if j != 'Q':
            break
    ans = min(ans,  len(line))

print(ans)

