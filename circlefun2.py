import turtle
from random import randint


wn = turtle.Screen()
wn.title('Hello, Circcle')
t = turtle.Turtle()

wn.colormode(255)
t.speed(10)


t.begin_fill()

for angle in range(0, 360, 15):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.seth(angle)
    t.circle(120)

t.end_fill()
wn.exitonclick()