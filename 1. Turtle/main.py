import turtle
import random

t = turtle.Turtle()

for n in range(50):

    size = random.randint(10, 100)

    def position():
        x = random.randint(-150, 150)
        y = random.randint(-150, 150)
        t.setposition(x, y)
        angle = random.randrange(360)
        t.setheading(angle)

    def square():
        t.penup()
        position()
        t.pendown()
        t.pencolor("red")
        for i in range(4):
            t.forward(size)
            t.left(90)

    def triangle():
        t.penup()
        position()
        t.pendown()
        t.pencolor("green")
        for i in range(3):
            t.forward(size)
            t.left(120)

    def circle():
        t.penup()
        position()
        t.pendown()
        t.pencolor("blue")
        for i in range(1):
            t.circle(size)

    shape = random.randrange(3)
    if shape == 1:
        square()
    elif shape == 2:
        triangle()
    else:
        circle()

turtle.exitonclick()
