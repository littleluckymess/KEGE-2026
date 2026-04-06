with open(r'./files/9_7030.txt') as file:
    data =[list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [2, 2, 2]:
        sides = sorted(set(line))
        a, b, c = sides
        if a ** 2 + b ** 2 == c ** 2:
            cnt += 1
    print(cnt)

