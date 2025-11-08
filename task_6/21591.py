from turtle import*
screensize(3000,3000)
tracer(False)
lt(90)
m=20
rt(270)
for i in range(2):
    fd(8*m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3*m)
    rt(240)
rt(240)
for i in range(2):
    fd(14*m)
    rt(120)
up()
for x in range(-8,7):
    for y in range(0,13):
        goto(x*m,y*m)
        dot(5,'red')
update()
done()