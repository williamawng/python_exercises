import turtle

wn = turtle.Screen()
wn.title("William star")
wn.bgcolor("light green")

turtle.color('red','yellow')

cnt = 0
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if cnt % 2 == 0:
        wn.bgcolor("light green")
    else:
        wn.bgcolor(0.68, 0.93, 0.93)
    cnt += 1
    # print(turtle.pos())
    if abs(turtle.pos()) < 1:
        break

turtle.end_fill()
turtle.done()