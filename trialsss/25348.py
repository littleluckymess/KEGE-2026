with open (r'./files/9_25348.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        pov = [i for i in line if line.count(i) != 1]
        ne_pov = [i for i in line if line.count(i) == 1]
        if max(line) == max(ne_pov):
            cnt +=1
print(cnt)
