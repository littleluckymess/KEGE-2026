with open (r'./files/9832.txt') as file:
    data = [list(map(int,i.split())) for i in file]

for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        if line.count(max(line)) == 1:
            print(sum(line))
            break




