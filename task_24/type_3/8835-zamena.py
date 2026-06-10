with open (r'../files/8835.txt') as file:
    data = file.readline()

data = data.split('M')

ans = 0
for i in range(len(data) - 112):
    line_1 = data[i]
    line = 'M' + 'M'.join(data[i + 1:i+112]) + 'M'
    line_113 = data[i+112]
    if line.count('.') != 0 or line_113.count('.') == 0: continue
    if '.' in line_1:
        line_1 = line_1[line_1.rfind('.') + 1:]
    line_113 = line_113[:line_113.find('.') + 1]
    line = line_1 + line + line_113
    ans = max(ans, len(line))
print(ans)
