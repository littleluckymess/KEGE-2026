with open(r'./files/17_17558.txt') as file:
    data = [int(i) for i in file]

cnt_32 = [i for i in data if abs(i) % 32 == 0]

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 < 0
    u2 = num2 < 0
    if u1 + u2 >= 1 and (num1 + num2) < len(cnt_32):
        ans.append(num1 + num2)
print(len(ans), max(ans))
