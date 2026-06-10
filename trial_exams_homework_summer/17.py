with open (r'files/17_23376.txt') as file:
    data = [int(i) for i in file]

max_37 = max(i for i in data if len(str(abs(i))) == 5 and abs(i) % 100 == 37)

ans = []

for num1, num2 in zip(data, data[1:]):
    u1 = len(str(abs(num1))) == 5
    u2 = len(str(abs(num2))) == 5
    if u1 + u2 == 1 and (num1 + num2)**2 > max_37 ** 2:
        ans.append(num1 + num2)
print(len(ans), max(ans))

