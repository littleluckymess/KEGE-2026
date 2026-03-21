with open (r'./files/17_9786.txt') as file:
    data = [int(i) for i in file]
max_25 = (max(i for i in data if abs(i) % 100 == 25))

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cnt = 0
    for num in num1, num2, num3:
        if len(str(abs(num))) == 4:
            cnt += 1
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    u3 = len(str(abs(num3))) == 4
    u4 = num1 + num2 + num3
    if u1 + u2 + u3 <= 2 and u4 <= max_25:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))

#####################################################

with open (r'./files/17_9786.txt') as file:
    data = [int(i) for i in file]
max_25 = (max(i for i in data if abs(i) % 100 == 25))

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cnt = 0
    for num in num1, num2, num3:
        if len(str(abs(num))) == 4:
            cnt += 1
    if cnt <= 2 and num1 + num2 + num3 <= max_25:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))

#####################################################

with open (r'./files/17_9786.txt') as file:
    data = [int(i) for i in file]
max_25 = (max(i for i in data if abs(i) % 100 == 25))

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    cnt = [num for num in (num1, num2, num3)  if len(str(abs(num))) == 4]
    if len(cnt) <= 2 and num1 + num2 + num3 <= max_25:
        ans.append(num1 + num2 + num3)

print(len(ans), max(ans))

######################################################

with open (r'./files/17_9786.txt') as file:
    data = [int(i) for i in file]
max_25 = (max(i for i in data if abs(i) % 100 == 25))

ans = []
for nums in zip(data, data[1:], data[2:]):
    cnt = [num for num in nums  if len(str(abs(num))) == 4]
    if len(cnt) <= 2 and sum(nums) <= max_25:
        ans += [sum(nums)]

print(len(ans), max(ans))