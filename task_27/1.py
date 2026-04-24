from math import *

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27138_a.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]


cluster_1 = [dot for dot in dots if dot[0] < 0]
cluster_2 = [dot for dot in dots if dot[0] > 0]

cen_1 = center(cluster_1)
cen_2 = center(cluster_2)

print(abs(cen_1[0] - cen_2[0]) * 10000)
print(abs(cen_1[1] - cen_2[1]) * 10000)



with open(r'.\files\27138.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 10:
        clusters.append(cluster)
print([len(cluster) for cluster in clusters])

print(max(clusters[2], key=lambda x: x[0])[0] * 10000)

max_x = -10**10

for i in clusters[2]:
    max_x = max(max_x, i[0])
print(max_x*10000)

dists = []
for dot in clusters[0]:
    sum_dist = sum(dist(dot, d) for d in clusters[1] + clusters[2])
    dists.append([sum_dist, dot])

for dot in clusters[1]:
    sum_dist = sum(dist(dot, d) for d in clusters[0] + clusters[2])
    dists.append([sum_dist, dot])

for dot in clusters[2]:
    sum_dist = sum(dist(dot, d) for d in clusters[1] + clusters[0])
    dists.append([sum_dist, dot])

print(sum(max(dists)[1]))



