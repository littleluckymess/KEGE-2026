ans=[]
for N in range(1,100000):
    R=bin(N)[2:]
    if N%3==0:
        R=R+R[-3:]
    else:
      R = R + f'{N%3*3:b}'
    R=int(R,2)
    if R<=170:
        ans.append(R)
print(max(ans))