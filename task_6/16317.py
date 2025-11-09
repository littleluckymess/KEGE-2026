from turtle import*
screensize(3000,3000)
tracer(False)
m=10
lt(90)
for i in range(2):
    fd(21*m)
    rt(90)
    fd(27*m)
    rt(90)
up()
fd(9*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in range(2):
    fd(86*m)
    rt(90)
    fd(47*m)
    rt(90)
up()
for x in range(0,58):
    for y in range(0,96):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()
