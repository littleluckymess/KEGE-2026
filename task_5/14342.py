for p in range(int(max('BOOMBLCNG'), 36) + 1, 37):
    num1 = int('bo', p)
    num2 = int('om', p)
    num3 = int('bl4', p)
    num4 = int('cng', p)
    if num1 + num2 + num3 == num4:
        print(p)






