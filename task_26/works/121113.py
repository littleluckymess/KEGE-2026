with open (r'..\files\26_12113.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)
red_traj= [max (i for i in boxes if i % 2 == 1)]
blue_traj= [max(boxes, key=lambda x: (x % 2 == 0, x))]

for box in boxes:
    if red_traj[-1] % 2 != box % 2 and red_traj[-1] - box >= 7:
        red_traj.append(box)
    if blue_traj[-1] % 2 != box % 2 and blue_traj[-1] - box >= 7:
        blue_traj.append(box)
print(len(red_traj), red_traj[-1])
print(len(blue_traj), blue_traj[-1])