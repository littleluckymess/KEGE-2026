from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open (r'./files/27_A-0932-p.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, info = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if info[:2] == 'L3':
            stars.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]

stars_1 = [d for d in stars if d[1] < 8]
stars_2 = [d for d in stars if d[1] > 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

A1 = []
for s in stars:
    A1.append(dist(center_2, s))

A2 = []
for s in stars:
    A2.append(dist(center_1, s))

print(max(A1) * 10_000)
print(max(A2) * 10_000)


