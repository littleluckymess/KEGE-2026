from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[1] == '3':
            stars.append(dots[-1])


cluster_1 = [d for d in dots if d[1] < 16]
cluster_2 = [d for d in dots if 16 < d[1] < 23]
cluster_3= [d for d in dots if d[1] > 23]


stars_1 = [d for d in stars if d[1] < 16]
stars_2 = [d for d in stars if 16 < d[1] < 23]
stars_3= [d for d in stars if d[1] > 23]

print(len(stars_1), len(stars_2), len(stars_3))

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print(dist(center_1, center_3) * 10_000)


