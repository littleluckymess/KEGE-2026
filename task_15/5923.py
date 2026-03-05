def DIG(x,y):
   return str(x)[0] == str(y)[0]

def f(x):
    return (not DIG(x,28) and DIG(x, 47)) <= (x > A - 20)
for A in range(1,1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
