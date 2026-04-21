from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

cluster_A_1 = [dot for dot in dots if 10/ 12 * dot[0] - 10 < dot[1]]
cluster_A_2 = [dot for dot in dots if -6 < dot[1] < 10/12 * dot[0] - 10]
cluster_A_3 = [dot for dot in dots if dot[1] < -6]
clusters = [cluster_A_1, cluster_A_2, cluster_A_3]

centers = [center(cluster) for cluster in clusters]
print(sum(c[0] for c in centers) / len(centers) * 10_000)
print(sum(c[1] for c in centers) / len(centers) * 10_000)


with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float,i.replace(',','.').split())) for i in file]

cluster_B_1 = [dot for dot in dots if dot[1] < -2*dot[0] - 26]
cluster_B_2 = [dot for dot in dots if dot[1] > -2*dot[0] - 26 and dot[0] < -10]
cluster_B_3 = [dot for dot in dots if dot[1] > 2*dot[0] + 14 and dot[0] > -10]
cluster_B_4 = [dot for dot in dots if dot[0] < dot[1] < 2*dot[0] + 14]
cluster_B_5 = [dot for dot in dots if -5 < dot[1] < dot[0]]
cluster_B_6 = [dot for dot in dots if dot[1] < -5]
clusters = [cluster_B_1, cluster_B_2, cluster_B_3, cluster_B_4, cluster_B_5, cluster_B_6]

centers = [center(cluster) for cluster in clusters]
print(sum(c[0] for c in centers) / len(centers) * 10_000)
print(sum(c[1] for c in centers) / len(centers) * 10_000)