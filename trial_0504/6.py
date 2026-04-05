from turtle import *
tracer(False)
screensize(3000, 3000)
m = 15
lt(90)

for i in range(4):
    fd(10 * m)
    rt(270)
up()
fd(3*m)
rt(270)
fd(5*m)
rt(90)
down()

for i in range(2):
    fd(10*m)
    rt(270)
    fd(12*m)
    rt(270)
up()

for x in range(-17, 1):
    for y in range(0, 14):
        goto(x*m, y*m)
        dot(3, 'purple')

update()
done()