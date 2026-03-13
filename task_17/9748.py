with open(r'.\files\17_9748.txt') as file:
    data = [int(i) for i in file]

max_15 = max(i for i in data if i % 100 == 15)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(num1)) == 4
    u2 = 1000 <= num2 <= 9999
    u3 = len(str(num3)) == 4
    u4 = num1 + num2 + num3

    if u1 + u2 + u3 == 1 and u4 >= max_15:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))
