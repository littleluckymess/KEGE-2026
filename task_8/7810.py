from itertools import product
cnt = 0
for val in product('МАСЛО',repeat=6):
    val = ''.join(val)
        cnt+=1
print(cnt)