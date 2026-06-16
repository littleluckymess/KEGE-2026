with open (r'./files/9_12241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 2, 2, 2]:
        pov = [i for i in line if line.count(i) % 2 == 0]
        ne_pov = [i for i in line if line.count(i) % 2 != 0]
        if (max(pov) + min(pov)) / 2 < sum(ne_pov):
            cnt += 1
print(cnt)
