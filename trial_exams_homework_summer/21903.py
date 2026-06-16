with open(r'./files/17_21903.txt') as file:
    data = [int(i) for i in file]

min_15 = min(i for i in data if abs(i) % 100 == 15 and len(str(abs(i))) == 3)

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = abs(num1) == abs(num2) == abs(num3)
    u2 = max(num1, num2, num3)
    u3 = min(num1, num2, num3)
    if u1 == 1 and u2 * u3 > min_15**2:
        ans.append(u2 * u3)
