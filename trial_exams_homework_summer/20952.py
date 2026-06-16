from turtle import*

screensize(3000,3000)
tracer(False)

m = 20

for i in range(5):
    fd(6 * m)
    rt(90)
    fd(3 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(2 * m)
rt(90)
down()
for i in range(8):
    fd(8 * m)
    rt(90)
    fd(5 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(2 * m)
lt(90)
down()
for i in range(4):
    fd(5 * m)
    lt(90)
up()

for x in range(0, 12):
    for y in range(-3, 6):
        goto(x * m, y * m)
        dot(5, 'white')
update()
done()