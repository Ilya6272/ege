from turtle import *
screensize(2000, 2000)
tracer(0)
m = 10
lt(90)


for i in range(2):
    fd(13 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()

fd(5 * m)
rt(90)
fd(9 * m)
lt(90)
down()

for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * m, y * m)
        dot(3, 'red')
done()
