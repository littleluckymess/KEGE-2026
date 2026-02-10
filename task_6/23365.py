from turtle import*
screensize(3000,3000)
tracer(False)

lt(90)
m = 10

for k in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)

up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()

for k in range(3):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)
up()

for x in range(0,49):
    for y in range(-17,40):
        goto(x*m, y*m)
        dot(5,'white')
update()
done()