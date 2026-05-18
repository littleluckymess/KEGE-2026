from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
with open(r'../files/24_21421.txt') as file:
    data = file.readline()

for i in alph[12:]:
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for line in data:
    line = line.lstrip('0').rstrip('13579B')
    ans = max(ans, len(line))
print(ans)


alph = digits + ascii_uppercase
with open(r'../files/24_21421.txt') as file:
    data = file.readline()

for i in alph[12:]:
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for line in data:
    while line and line[0] == '0':
        line = line[1:]
    while line and line[-1] in '13579B':
        line = line[:-1]
    ans = max(ans, len(line))
print(ans)