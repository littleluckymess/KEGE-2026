with open(r'./files/17_28938.txt') as file:
    data = [int(i) for i in file]

max_28 = max(i for i in data if abs(i) % 100 == 28)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) == 3
    u2 = len(str(abs(num2))) == 3
    u3 = len(str(abs(num3))) == 3
    u4 = (num1 + num2 + num3) / 3
    if u1 + u2 + u3 >= 1 and 0 < u4 < max_28:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))