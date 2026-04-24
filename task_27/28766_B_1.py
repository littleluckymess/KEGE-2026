from itertools import combinations
from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x, y])))

cluster_1 = [[d for d in dots if 23 < d[1]],
             [d for d in stars if 23 < d[1]]]
cluster_2 = [[d for d in dots if 16 < d[1] < 23],
             [d for d in stars if 16 < d[1] < 23]]
cluster_3 = [[d for d in dots if d[1] < 16],
             [d for d in stars if d[1] < 16]]
clusters = [cluster_1, cluster_2, cluster_3]

B1 = []
for cluster in clusters:
    B1 += [dist(s1, s2) for s1, s2 in combinations(cluster[1], 2)]

min_center = center(min(clusters, key=lambda x: len(x[1]))[0])
max_center = center(max(clusters, key=lambda x: len(x[1]))[0])

print(min(B1) * 10_000)
print(dist(min_center, max_center) * 10_000)




