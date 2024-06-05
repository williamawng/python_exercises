import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("William")

star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(100):
    star.right(190)
    star.forward(100)

turtle.done()