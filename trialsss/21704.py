with open (r'./files/9_21704.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for line in data:
    line = sorted(line)[::-1]
    if (max(line) + min(line)) / 2 > (sum(line) - (max(line) + min(line))) / 5:
        print(line, sum(line))
        break

