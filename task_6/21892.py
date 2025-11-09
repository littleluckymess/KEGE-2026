from turtle import*
screensize(3000,3000)
tracer(False)
m=8
rt(90)
for i in range(7):
   rt(45)
   fd(11*m)
   rt(45)
up()
for x in range(-15,1):
    for y in range(-8,9):
        goto(x*m,y*m)
        dot(3,'red')
update()
done()
