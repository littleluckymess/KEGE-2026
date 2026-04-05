with open(r'files/17.txt') as file:
    data = [int(i) for i in file]

maxx_2 = max(i for i in data if len(str(i)) == 2)

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = len(str(num1)) == 2
    u2 = len(str(num2)) == 2
    if u1 + u2 == 1 and (num1 + num2) % maxx_2 == 0:
        ans += ([num1 + num2])
print(len(ans), max(ans))
