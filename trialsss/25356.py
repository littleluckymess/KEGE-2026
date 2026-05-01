with open(r'./files/17_25356.txt') as file:
    data = [int(i) for i in file]

max_30 = max(i for i in data if abs(i) % 100 == 30)

ans =[]
for num1, num2, num3 in (zip(data, data[1:], data[2:])):
    u1 = len(str(abs(num1))) == 4
    u2= len(str(abs(num2))) == 4
    u3 = len(str(abs(num3))) == 4
    u4 = num1 + num2 + num3

    if u1 + u2 + u3 == 0 and u4 > max_30:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))


