with open (r'../files/26.2_19727.txt') as file:
    M, N = map(int, file.readline().split())
    delivery = [int(i) for i in file]

delivery = sorted(delivery)

ans = []
for bidon in delivery:
    if sum(ans) + bidon <= M:
        ans.append(bidon)
free_space = M - sum(ans[:-1])

print(len(ans), len([i for i in delivery if i > free_space]))
print(len(ans), sum(i > free_space for i in delivery))