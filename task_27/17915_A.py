from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = [sum(dist(dot, d) for d in cluster)]
        res.append([sum_dist, dot])
    return min(res)[1]

with open (r'./files/27_A_17915.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_1 = [dot for dot in dots if 0< dot[0] < 6 and 21 < dot[1] < 27]
cluster_2 = [dot for dot in dots if 8 < dot[0] < 14 and 23 < dot[1] < 29]
cluster_3 = [dot for dot in dots if 12 < dot[0] < 18 and 16 < dot[1] < 23]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print((center_1[0] + center_2[0] + center_3[0])/3* 10_000)
print((center_1[1] + center_2[1] + center_3[1])/3* 10_000)
