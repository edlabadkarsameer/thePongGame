import turtle

# Create the game window
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle class
class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        y = self.ycor()
        if y < 250:
            y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        if y > -240:
            y -= 20
        self.sety(y)

# Ball class
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.2  # Ball's x-axis movement speed
        self.dy = 0.2  # Ball's y-axis movement speed

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.dx *= -1

# Create paddles
paddle_a = Paddle(-350, 0)
paddle_b = Paddle(350, 0)

# Create the ball
ball = Ball()

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a.move_up, "w")
window.onkeypress(paddle_a.move_down, "s")
window.onkeypress(paddle_b.move_up, "Up")
window.onkeypress(paddle_b.move_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.move()

    # Check for collision with paddles
    if ball.xcor() > 340 and ball.distance(paddle_b) < 50 or ball.xcor() < -340 and ball.distance(paddle_a) < 50:
        ball.bounce_x()

    # Check for collision with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Check for scoring
    if ball.xcor() > 390:
        ball.reset_position()
        # Increment player A's score here

    if ball.xcor() < -390:
        ball.reset_position()
        # Increment player B's score here

