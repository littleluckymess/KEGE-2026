
from turtle import *
tracer(False)
screensize(3000, 3000)
m = 20
lt(90)

for i in range(5):
    fd(15 * m)
    lt(90)
    fd(25 * m)
    lt(90)
up()
fd(4 * m)
lt(90)
fd(12 * m)
lt(90)
down()
for i in range(6):
    fd(38 * m)
    rt(90)
    fd(22 * m)
    rt(90)
up()
for x in range(-13, 1):
    for y in range(11, 16):
        goto(x*m, y*m)
        dot(10, 'white')
update()
done()