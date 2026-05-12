from turtle import*
screensize(3000, 3000)
tracer(False)
m = 10

for i in range(6):
    fd(71*m)
    rt(90)
    fd(73*m)
    rt(90)
up()
fd(18*m)
rt(90)
fd(22*m)
lt(90)
down()
for i in range(6):
    fd(45*m)
    rt(90)
    fd(58*m)
    rt(90)
up()
for x in range(18, 64):
    for y in range(-73, -21):
        goto(x*m, y*m)
        dot(3, 'purple')
update()
done()