with open(r'..\files\26_5988.txt') as file:
    N = int(file.readline())
    boxes = []
    for line in file:
        size, color = line.split()
        boxes.append((int(size), color))

boxes = sorted(boxes)

max_boxes_by_colors = {'R': [0, -6, 10 ** 4], 'G': [0, -6, 10 ** 4], 'B': [0, -6, 10 ** 4]}
for box in boxes:
    copy_max_boxes_by_colors = max_boxes_by_colors.copy()
    del copy_max_boxes_by_colors[box[1]]
    last_box = max(copy_max_boxes_by_colors.values(), key=lambda x: (box[0] - x[1] >= 7, x[0], x[1]))
    if box[0] - last_box[1] >= 7 and max_boxes_by_colors[box[1]][0] < last_box[0] + 1:
        max_boxes_by_colors[box[1]] = [last_box[0] + 1, box[0], min(box[0], last_box[2])]




