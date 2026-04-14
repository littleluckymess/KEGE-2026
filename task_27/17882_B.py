from math import dist

def center (cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open (r'./files/27_B_17882.txt') as file:
    dots =[list(map(float, i.split())) for i in file]

cluster_1 = [dot for dot in dots if dot[1] < 3]
cluster_2 = [dot for dot in dots if dot[1] > 7]
cluster_3 = [dot for dot in dots if dot[0] > 5]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

print((center_1[0] + center_2[0] + center_3[0]) / 3 * 10_000)
print((center_1[1] + center_2[1] + center_3[1]) / 3 * 10_000)



