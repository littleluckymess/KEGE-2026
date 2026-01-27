from turtle import*
screensize(3000,3000)
tracer(False)
m = 10

for i in range(13):
    fd(13*m)
    rt(90)
    fd(5*m)
up()
rt(90)
fd(7*m)
lt(90)
fd(10*m)
down()

for i in range(23):
    fd(8*m)
    lt(90)
    fd(11*m)
    lt(90)
up()

for x in range(-5,18):
    for y in range(-23,1):
        goto(x*m, y*m)
        dot (3, 'purple')
update()
done()
