from turtle import *

t = Turtle()
s = Screen()

t.speed(1)

loop = int(input("how many loops?"))
color = input("what color? red/green/blue? ")

if color =="red":
  t.pencolor("red")
if color =="green":
  t.pencolor("green")
if color =="bue":
  t.pencolor("blue")
  
for i in range(loop):
  t.forward(70)
  t.left(360/loop)