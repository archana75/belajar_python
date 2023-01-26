from turtle import *

turtle = Turtle()
screen = Screen()

turtle.pencolor("yellow")
turtle.fillcolor("cyan")
turtle.width(5)

turtle.begin_fill()
turtle.speed(1)
turtle.forward(50)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()