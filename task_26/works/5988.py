with open (r'../files/26_5988.txt') as file:
    N = int(file.readline())
    boxes = []
    for line in file:
        size, color = line.split()
        boxes.append((int(size), color))

boxes = sorted(boxes, reverse=True)



