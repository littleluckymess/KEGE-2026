with open (r'files/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
        if max(line) < sum(line) - max(line):
            cnt += 1
print(cnt)