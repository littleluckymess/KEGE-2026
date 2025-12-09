alph = sorted('СОЛНЦЕ')
cnt = 0
for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
        cnt +=1
print(cnt)