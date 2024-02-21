import turtle

# Set up the window
window = turtle.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width=600, height=400)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=1, stretch_len=5)
paddle_b.penup()
paddle_b.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2  # Ball movement speed along the x-axis
ball.dy = 2  # Ball movement speed along the y-axis

# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 190:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -190:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 190:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -190:
        paddle_b.sety(y - 20)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1  # Reverse the direction if the ball hits the top or bottom border

    # Paddle collisions
    if (
        (ball.xcor() > 240 and ball.xcor() < 250)
        and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50)
    ) or (
        (ball.xcor() < -240 and ball.xcor() > -250)
        and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50)
    ):
        ball.dx *= -1  # Reverse the direction if the ball hits a paddle
