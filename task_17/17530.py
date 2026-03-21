with open (r'./files/17_17530.txt') as file:
    data = [int(i) for i in file]
minn = (min(i for i in data))
