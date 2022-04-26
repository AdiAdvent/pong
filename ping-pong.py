#ping-pong

import turtle
import winsound #https://docs.python.org/3/library/winsound.html

win = turtle.Screen()
win.title("ping-pong")
win.setup(width=1200, height=900)
win.bgcolor("black")
win.tracer(0)


#Player1
pOne = turtle.Turtle()
pOne.speed(0)
pOne.shape("square")
pOne.color("white")
pOne.shapesize(stretch_len=1, stretch_wid=4)
pOne.up()
pOne.goto(-595,0)


#Player2
pTwo = turtle.Turtle()
pTwo.speed(0)
pTwo.shape("square")
pTwo.color("white")
pTwo.shapesize(stretch_len=1, stretch_wid=4)
pTwo.up()
pTwo.goto(595,0)

if pOne.ycor() > 250:
    pOne.sety(250)

if pTwo.ycor() > 250:
    pTwo.sety(250)

if pOne.ycor() < -250:
    pOne.sety(-250)

if pTwo.ycor() < -250:
    pTwo.sety(-250)


#Puck
puck = turtle.Turtle()
puck = turtle.Turtle()
puck.speed(0)
puck.shape("circle")
puck.color("white")
puck.up()
puck.goto(0,0)

puck.dx = 1/4
puck.dy = 1/4


#function
def pOneUp():
    y = pOne.ycor()
    y += 20
    pOne.sety(y)

def pOneDn():
    y = pOne.ycor()
    y -= 20
    pOne.sety(y)

def pTwoUp():
    y = pTwo.ycor()
    y += 20
    pTwo.sety(y)

def pTwoDn():
    y = pTwo.ycor()
    y -= 20
    pTwo.sety(y)


#Scoreboard
scoreA = 0
scoreB = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.up()
pen.hideturtle()
pen.goto(0,-444)

pen.write("Player 1: 0 Player 2: 0", align="center", font = 22)


win.listen()
win.onkeypress(pOneUp, "w")
win.onkeypress(pOneDn, "s")
win.onkeypress(pTwoUp, "p")
win.onkeypress(pTwoDn, "l")



#Gameplay
while True:
    win.update()

    #Puck movements
    puck.setx(puck.xcor() + puck.dx)
    puck.sety(puck.ycor() + puck.dy)

    #Great walls
    if puck.ycor() > 440:
        puck.sety(440)
        puck.dy *= -1

    if puck.xcor() > 590:
        puck.goto(0,0)
        puck.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(scoreA, scoreB), align="center", font = 22)

    if puck.ycor() < -440:
        puck.sety(-440)
        puck.dy *= -1

    if puck.xcor() < -590:
        puck.goto(0,0)
        puck.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(scoreA, scoreB), align="center", font = 22)

    

