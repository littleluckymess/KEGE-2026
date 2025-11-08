from turtle import*
screensize(3000,3000)
tracer(False)
m=15
for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)
up()
for x in range(-32,23):
    for y in range(-6,75):
        goto(x*m,y*m)
        dot(5,'white')
update()
done()