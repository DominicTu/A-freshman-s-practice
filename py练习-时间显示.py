import turtle
from datetime import datetime

def darwLine(darw):
    turtle.pendown() if darw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)

def drawDigit(x):
    darwLine(True) if x in [2, 3, 4, 5, 6, 8, 9] else darwLine(False)
    darwLine(True) if x in [0, 1, 3, 4, 5, 6, 7, 8, 9] else darwLine(False)
    darwLine(True) if x in [0, 2, 3, 5, 6, 8, 9] else darwLine(False)
    darwLine(True) if x in [0, 2, 6, 8] else darwLine(False)
    turtle.left(90)
    darwLine(True) if x in [0, 4, 5, 6, 8, 9] else darwLine(False)
    darwLine(True) if x in [0, 2, 3, 5, 6, 7, 8, 9] else darwLine(False)
    darwLine(True) if x in [0, 1, 2, 3, 4, 7, 8, 9] else darwLine(False)
    turtle.penup()
    turtle.left(180)
    turtle.fd(30)

def drawDate(date):
    for i in date:
        drawDigit(eval(i))   

def main():
    turtle.setup(1600,800,0,0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-265,0)
    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.speed(10)
    someday = datetime.now()
    day = someday.strftime("%Y%m%d")
    drawDate(day)

main()
