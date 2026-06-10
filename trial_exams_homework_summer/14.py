for x in range(1, 10):
    num = 2*2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35
    cnt = 0
    while num:
        if num % 49 == 0:
            cnt += 1
        num //=49
        
