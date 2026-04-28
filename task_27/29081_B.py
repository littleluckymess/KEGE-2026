from math import dist
from itertools import combinations

with open(r'./files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if int(data[1]) >= 8 and data[1] in '89' and data[1] >= '8':
            stars.append(dots[-1])

stars_1 = [d for d in stars if d[1] < 16]
stars_2 = [d for d in stars if 16 < d[1] < 23]
stars_3= [d for d in stars if d[1] > 23]

B1 = []
for s1 in stars_1:
    for s2 in stars_2:
        B1.append(dist(s1, s2))

for s1 in stars_1:
    for s3 in stars_3:
        B1.append(dist(s1, s3))

for s2 in stars_2:
    for s3 in stars_3:
        B1.append(dist(s2, s3))

B1 = min(B1)

B2 = []
for s1 in stars_1:
    for s2 in stars_1:
        if s1 != s2:
            B2.append(dist(s1, s2))
for s1 in stars_2:
    for s2 in stars_2:
        if s1 != s2:
            B2.append(dist(s1, s2))
for s1 in stars_3:
    for s2 in stars_3:
        if s1 != s2:
            B2.append(dist(s1, s2))


B2 = sum(B2) / len(B2)

print(B1 * 10_000, B2 * 10_000)

#############################################

stars_1 = [d for d in stars if 23 < d[1]]
stars_2 = [d for d in stars if 16 < d[1] < 23]
stars_3 = [d for d in stars if d[1] < 16]
all_stars = [stars_1, stars_2, stars_3]

B1 = [dist(s1, s2) for cl1, cl2 in combinations(all_stars, 2) for s1 in cl1 for s2 in cl2]
B2 = [dist(s1, s2) for cl in all_stars for s1, s2 in combinations(cl, 2)]

print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)

############################################

B1, B2 = [], []
for s1, s2 in combinations(stars, 2):
    u = any(s1 in cl and s2 in cl for cl in all_stars)
    d = dist(s1, s2)
    if u: B2.append(d)
    else: B1.append(d)

print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)
