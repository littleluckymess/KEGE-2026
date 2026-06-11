with open (r'./files/9_23368.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 1]:
        if (max(line) + min(line))*2 == (sum(line) - (max(line) + min(line)))*3:
            print(pos)
