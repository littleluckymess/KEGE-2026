with open(r'..\files\26_16390.txt') as file:
    S, N = map(int, file.readline().split())
    boxes = [int(i) for i in file]

boxes = sorted(boxes)

ans =[]
for box in boxes:
    if sum(ans) + box <= S:
        ans.append(box)


free_space = S - sum(ans[:-1])

print(len(ans), max(i for i in boxes if i <= free_space))
