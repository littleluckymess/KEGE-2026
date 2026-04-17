from math import dist
def center(cluster):
    res =[]
    for dot in cluster:
        sum_dist = sum(dist(d, dot) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open (r'./files/27_A_23209.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

cluster_A_1 = [dot for dot in dots if dot[0] < 5]
cluster_A_2 = [dot for dot in dots if dot[0] > 5]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)

print((max(center_A_1[0], center_A_2[0]) * 10_000))
print((max(center_A_1[1], center_A_2[1]) * 10_000))


with open (r'./files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [dot for dot in dots if 0 < dot[1] < 15]
cluster_B_2 = [dot for dot in dots if  15 < dot[1] < 21]
cluster_B_3 = [dot for dot in dots if  21 < dot[1] < 30]


center_B_1 = center(cluster_B_1)
center_B_2 = center(cluster_B_2)
center_B_3 = center(cluster_B_3)


print(len(cluster_B_1), len(cluster_B_2), len(cluster_B_3))

print((center_B_1[0] - center_B_3[0]) * 10_000)
print((center_B_1[1] - center_B_3[1]) * 10_000)

with open (r'./files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]
cluster_B_1 = [d for d in dots if 0 < d[1] < 15]
cluster_B_2 = [d for d in dots if 15 < d[1] < 21]
cluster_B_3 = [d for d in dots if 21 < d[1] < 30]
clusters_B = [cluster_B_1, cluster_B_2, cluster_B_3]

max_cluster = center(max(clusters_B, key=len))
min_cluster = center(min(clusters_B, key=len))

print((max_cluster[0] - min_cluster[0]) * 10_000)
print((max_cluster[1] - min_cluster[1]) * 10_000)


