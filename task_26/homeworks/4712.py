with open (r'../files/26_4712.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

answer = [boxes[0]]
for box in boxes:
    if answer[-1] - box >= 3:
        answer += [box]

print(len(answer), answer[-1])

