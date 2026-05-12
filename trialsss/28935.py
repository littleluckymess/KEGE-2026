from string import printable as p

for x in p[:23]:
    num1 = int(f'761{x}035', 23)
    num2 = int(f'338{x}932', 23)
    num = num1 + num2
    if num % 22 == 0:
        print(num//22)