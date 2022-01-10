import turtle

class Shape:
    def position(self):
        position_x = int(input('Zadaj pozíciu x: '))
        position_y = int(input('Zadaj pozíciu y: '))
        turtle.setposition(position_x, position_y)
    def setColor(self):
        color = str(input('Vyber farbu (red; green; blue): '))
        if color == 'red':
            turtle.pencolor("red")
        elif color == 'green':
            turtle.pencolor("green")
        elif color == 'blue':
            turtle.pencolor("blue")

class Rectangle(Shape):
    def draw(self):
        turtle.penup()
        self.position()
        turtle.pendown()
        self.setColor()
        for i in range(2):
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)

class Triangle(Shape):
    def draw(self):
        turtle.penup()
        self.position()
        turtle.pendown()
        self.setColor()
        for i in range(3):
            turtle.forward(75)
            turtle.left(120)

class Circle(Shape):
    def draw(self):
        turtle.penup()
        self.position()
        turtle.pendown()
        self.setColor()
        for i in range(1):
            turtle.circle(25)

rectangle = Rectangle()
triangle = Triangle()
circle = Circle()

def main():
    while True:
        print('Vyber si čo chceš vykresliť')
        print('Obdĺžnik......1')
        print('Trojuholník...2')
        print('Kurh..........3')
        choice = int(input())
        if choice == 1:
            rectangle.draw()
        elif choice == 2:
            triangle.draw()
        elif choice == 3:
            circle.draw()
        else:
            break

if __name__ == "__main__":
    main()

turtle.exitonclick()