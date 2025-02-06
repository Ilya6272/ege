from turtle import *

screensize(2000, 2000)
tracer(0)
lt(90)
m = 15

for i in range(2):
    fd(13 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
fd(8 * m)
rt(90)
bk(3 * m)
lt(90)
down()

for i in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)

up()
for x in range(-20, 40):
    for y in range(-10, 40):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()




