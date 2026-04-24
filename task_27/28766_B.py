from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open (r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x,y])))
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append(list(map(float, [x,y])))
cluster_B_1 = [dot for dot in dots if dot[1] > 25]
cluster_B_2 = [dot for dot in dots if 15 < dot[1] < 25]
cluster_B_3 = [dot for dot in dots if dot[1]< 15]


s_cluster_B_1 = [dot for dot in stars if dot[1] > 25]
s_cluster_B_2 = [dot for dot in stars if 15 < dot[1] < 25]
s_cluster_B_3 = [dot for dot in stars if dot[1]< 15]

B1 = []
for s1 in s_cluster_B_1:
    for s2 in s_cluster_B_1:
        if s1 != s2:
            B1.append(dist(s1, s2))
for s1 in s_cluster_B_2:
    for s2 in s_cluster_B_2:
        if s1 != s2:
            B1.append(dist(s1, s2))
for s1 in s_cluster_B_3:
    for s2 in s_cluster_B_3:
        if s1 != s2:
            B1.append(dist(s1, s2))
print(min(B1) * 10_000)


print(len(s_cluster_B_1), len(s_cluster_B_2), len(s_cluster_B_3))

B2 = dist(center(cluster_B_2), center(cluster_B_3))

print(B2 * 10_000)

