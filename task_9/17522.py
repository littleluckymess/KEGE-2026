with open (r'./files/17522.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if max(line) < sum(line) - max(line):
            u1 = line[0] == line[1]
            u2 = line[0] == line[2]
            u3 = line[0] == line[3]
            u4 = line[1] == line[2]
            u5 = line[1] == line[3]
            u6 = line[2] == line[3]
            if u1+u2+u3+u4+u5+u6 == 1:
                cnt += 1
print(cnt)