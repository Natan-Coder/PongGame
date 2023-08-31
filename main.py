# Pong Game #
import turtle

# Setup game screen
turtle.setup(400, 300)
# Set game background color
turtle.bgcolor("black")

# Left Paddle (Paddle 1)
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("red")
paddle1.shapesize(stretch_wid=4, stretch_len=1)  # make the paddle wider
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.dy = 0

# Right Paddle (Paddle 2)
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_wid=4, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)
paddle2.dy = 0

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Game Rules
game_over = False
winner = None
points = {
    "player1": 0,
    "player2": 0
}
game_rules = {
    "max_points": 3,
    "ball_speed": 3
}

# Score Display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 24, "normal"))

# Game Mechanics loop
ball_dx = 2
ball_dy = 3

paddle1.sety(paddle1.ycor() + paddle1.dy)
paddle2.sety(paddle2.ycor() + paddle2.dy)
ball.setx(ball.xcor() + ball_dx)
ball.sety(ball.ycor() + ball_dy)

# Check for game over conditions
if points["player1"] == game_rules["max_points"]:
    game_over = True
    winner = "player1"
elif points["player2"] == game_rules["max_points"]:
    game_over = True
    winner = "player2"

# Check ball collision with paddles
if (340 < ball.xcor() < 350) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
    ball.setx(340)
    ball_dx *= -1
elif (-340 > ball.xcor() > -350) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
    ball.setx(-340)
    ball_dx *= -1

# Check for ball moving offscreen
if ball.xcor() > 390:
    ball.goto(0, 0)
    ball_dx *= -1
    points["player1"] += 1
elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball_dx *= -1
    points["player2"] += 1

# Check for ball colliding with top/bottom frame
if ball.ycor() > 290:
    ball.sety(290)
    ball_dy *= -1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball_dy *= -1

# Update scoreboard
score_display.clear()
score_display.write("Player 1: {}  Player 2: {}".format(points["player1"], points["player2"]), align="center",
                    font=("Arial", 24, "normal"))


# Function to move paddle1 up
def paddle1_up():
    paddle1.dy = 10


# Function to move paddle1 down
def paddle1_down():
    paddle1.dy = -10


# Function to move paddle2 up
def paddle2_up():
    paddle2.dy = 10


# Function to move paddle2 down
def paddle2_down():
    paddle2.dy = -10


# Set up keyboard bindings
turtle.listen()
turtle.onkeypress(paddle1_up, "w")
turtle.onkeypress(paddle1_down, "s")
turtle.onkeypress(paddle2_up, "Up")
turtle.onkeypress(paddle2_down, "Down")

# Game over screen
game_over_display = turtle.Turtle()
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write("Game Over! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))

turtle.done()

