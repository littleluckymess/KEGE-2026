with open(r'./files/9_28930.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    if sorted(set(line)) == line and (min(line) + max(line)) <= sum(line) - (min(line) + max(line)):
        cnt += 1
print(cnt)