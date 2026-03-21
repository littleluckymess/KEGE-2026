with open(r'../files/26_5066.txt') as file:
    N = int(file.readline())
    containers = [int(i) for i in file]

containers = sorted(containers, reverse=True)

blocks = []
while containers:
    block = [containers[0]]
    containers.remove(containers[0])
    for container in containers.copy():
        if block[-1] - container >= 7:
            block += [container]
            containers.remove(container)
    blocks += [len(block)]

print(len(blocks), max(blocks))