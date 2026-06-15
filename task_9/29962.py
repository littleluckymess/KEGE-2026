with open(r'./files/9_29962.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        pov = [i for i in line if line.count(i)  > 1]
        ne_pov = [i for i in line if line.count(i) == 1]
        if sum(ne_pov)/len(ne_pov) > pov[0]:
            print(pos)



