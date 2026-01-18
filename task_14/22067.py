num = 3*17**777 + 15*17**250 - 6*17**100 + 2
ans=[]
while num:
    if num % 17 % 2 ==0:
        ans.append(num % 17)
    num //=17
print(len(set(ans)))
