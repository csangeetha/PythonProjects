# Practising Python 3 with tutorials from TokyoEdTech to build pong game
# Inspired from freeCodeCamp tutorials by building games to understand and learn various python modules

#Module for graphics
import turtle
import os

#building the window layout using the Screen() from turtle module
windowLayout = turtle.Screen()
windowLayout.title("Ping Pong game")
windowLayout.bgcolor("white")
windowLayout.setup(width=800, height=600)
windowLayout.tracer(0)


# Racket one
racket_one = turtle.Turtle()
racket_one.speed(0)
racket_one.shape("square")
racket_one.shapesize(stretch_wid=5,stretch_len=1)
racket_one.color("black")
racket_one.penup()
racket_one.goto(-350, 0)
# Racket two

racket_two = turtle.Turtle()
racket_two.speed(0)
racket_two.shape("square")
racket_two.shapesize(stretch_wid=5,stretch_len=1)
racket_two.color("black")
racket_two.penup()
racket_two.goto(350, 0)

# Ping Pong ppball
ppball = turtle.Turtle()
ppball.speed(0)
ppball.shape("square")
ppball.color("black")
ppball.penup()
ppball.goto(0, 0)
ppball.dx = 2
ppball.dy = 2

# Score Board on the screen
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.color("black")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 260)
scoreBoard.write("Player One: 0  Player Two: 0", align="center", font=("Serif", 24, "normal"))

# Track score
player_one_score = 0
player_two_score = 0

# Motions of the elements on the board, grouping into functions
def paddle_a_up():
    y = racket_one.ycor()
    y += 20
    racket_one.sety(y)

def paddle_a_down():
    y = racket_one.ycor()
    y -= 20
    racket_one.sety(y)

def paddle_b_up():
    y = racket_two.ycor()
    y += 20
    racket_two.sety(y)

def paddle_b_down():
    y = racket_two.ycor()
    y -= 20
    racket_two.sety(y)

# Keyboard events and binding them to keys
windowLayout.listen()
windowLayout.onkeypress(paddle_a_up, "Up")
windowLayout.onkeypress(paddle_a_down, "Down")
windowLayout.onkeypress(paddle_b_up, "w")
windowLayout.onkeypress(paddle_b_down, "s")

# Loop for Main game 
while True:
    windowLayout.update()
    
    # Move the ppball
    ppball.setx(ppball.xcor() + ppball.dx)
    ppball.sety(ppball.ycor() + ppball.dy)

    # Border checking

    # Top and bottom
    if ppball.ycor() > 290:
        ppball.sety(290)
        ppball.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif ppball.ycor() < -290:
        ppball.sety(-290)
        ppball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ppball.xcor() > 350:
        player_one_score += 1
        scoreBoard.clear()
        scoreBoard.write("Player One: {}  Player Two: {}".format(player_one_score, player_two_score), 
        align="center", font=("Serif", 24, "normal"))
        ppball.goto(0, 0)
        ppball.dx *= -1

    elif ppball.xcor() < -350:
        player_two_score += 1
        scoreBoard.clear()
        scoreBoard.write("Player One: {}  Player Two: {}".format(player_one_score, player_two_score), 
        align="center", font=("Serif", 24, "normal"))
        ppball.goto(0, 0)
        ppball.dx *= -1

    # Rackets and ppball collisions
    if ppball.xcor() < -340: 
        if ppball.ycor() < racket_one.ycor() + 50: 
            if ppball.ycor() > racket_one.ycor() - 50:
                ppball.dx *= -1 
                os.system("afplay bounce.wav&")
    
    elif ppball.xcor() > 340:
        if ppball.ycor() < racket_two.ycor() + 50:
            if ppball.ycor() > racket_two.ycor() - 50:
                ppball.dx *= -1
                os.system("afplay bounce.wav&")



