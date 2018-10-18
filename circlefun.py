import turtle
from random import randint


wn = turtle.Screen()
wn.title('Hello, Turtle')
t = turtle.Turtle()

wn.colormode(255)
t.speed(10)


t.begin_fill()

for i in range(1000):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    t.forward(i)
    t.left(90)

t.end_fill()
wn.exitonclick()