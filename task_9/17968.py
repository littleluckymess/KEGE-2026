with open(r'./files/9_17968.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    if max(line) < sum(line) - max(line):
        chet = [i for i in line if i % 2 == 0]
        ne_chet = [i for i in line if i % 2 == 1]
        if sum(chet) == sum(ne_chet):
            cnt += 1
print(cnt)