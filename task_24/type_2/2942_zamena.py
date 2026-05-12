with open (r'../files/24_2942.txt') as file:
    data = file.readline()

data = data.replace('AB', '*')
data = data.replace('AC', '*')

for i in 'ABC':
    data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))
