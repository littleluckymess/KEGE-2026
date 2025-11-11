from turtle import*
screensize(3000,3000)
tracer(False)
lt(90)
m=10
for i in range(9):
    fd(30*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
lt(270)
fd(5*m)
lt(90)
down()
for i in range(2):
    fd(24*m)
    rt(90)
    fd(28*m)
    rt(90)
up()
for x in range(-21,18):
    for y in range(0,31):
        goto(x*m,y*m)
        dot(10,'white')
update()
done()