with open(r'./files/17_12249.txt') as file:
    data = [int(i) for i in file]

max_3 = (max(i for i in data if abs(i) % 10 == 3 and len(str(abs(i))) == 5))

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = abs(num1) % 10 == 3
    u2 = abs(num2) % 10 == 3
    u3 = abs(num3) % 10 == 3
    u4 = num1 + num2 + num3
    if u1 + u2 + u3 >= 1 and u4 <= max_3:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))

