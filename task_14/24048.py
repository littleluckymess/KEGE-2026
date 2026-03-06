def convert_10(num, sys):
    num = num [::-1]
    summ = 0
    for i in range(len(num)):
        summ += int(num[i], 36)*sys**i
    return summ


for p in range(33, 100):
    num1 = convert_10('KOT', p)
    num2 = convert_10('GOLODNI',p)
    num3 = convert_10('MEEOW', p)
    num4 = convert_10('100',p)
    if num1 + num2 == num3 * num4 - 20194023088:
        print(convert_10('PURR',p))

