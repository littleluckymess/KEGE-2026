from math import dist

with open (r'files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, info = i.replace(',','.').split()
        dots.append([float(x), float(y)])
        if int(info[1]) >= 8:
            stars.append(dots[-1])


stars_1 = [d for d in stars if d[1] < 15]
stars_2 = [d for d in stars if 15 < d[1] < 22]
stars_3 = [d for d in stars if d[1] > 22]

B1 = []
for s1 in stars_1:
    for s2 in stars_2:
        B1.append(dist(s1, s2))

for s1 in stars_2:
    for s2 in stars_3:
        B1.append(dist(s1, s2))

for s1 in stars_3:
    for s2 in stars_1:
        B1.append(dist(s1, s2))

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

print(min(B1) * 10_000, sum(B2)/len(B2) * 10_000)