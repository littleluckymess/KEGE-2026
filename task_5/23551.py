for N in range(1,100_000):
    R = bin(N)[2:]
    if int(R)%2==0:
        R='10'+R[2:]
    else:
        R='1'+R[2:]+'01'
    R=int(R,2)
    if R<30:
        print(N)
        break