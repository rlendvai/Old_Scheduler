from turtle import *
import math
import itertools
global screen
screen = Screen()
screen.tracer(50,0)


'''turtle=Turtle()
s = Shape("compound")
poly1 = ((10,-5),(0,10),(-10,-5),(3,3))
s.addcomponent(poly1, "red", "blue")
#poly2 = ((0,0),(10,-5),(-10,-5))
#s.addcomponent(poly2, "blue", "red")

turtle.screen.register_shape("myshape", s)
turtle.shape("myshape")
turtle.left(90)
turtle.forward(10)
print(turtle.xcor(), turtle.ycor())
'''

class Grid():
    def __init__(self):
        g = Turtle()
        g.shape('circle')
        g.color('red')
        g.setx(0)
        g.sety(0)
        g.shapesize(.1,.1,0)

        for i in range (-400,400,10):
            self.line(i,'vertical')
            self.line(i, 'horizontal')

    def line (self, coordinate, direction = 'vertical'):
        line = Turtle()
        line.penup()
        line.color('grey')
        offset = 7
        if direction == 'vertical':
            x = coordinate
            line.left(90)
            line.setx(x + offset)
            line.sety(0)
            if(x%50 ==0):
                if x!= 0:
                    line.write(str(x))
                line.pensize(2)
            line.setx(x)
        elif direction == 'horizontal':
            y = coordinate
            line.sety(y + offset)
            line.setx(0 + offset)
            if(y%50 == 0):
                line.write(str(y))
                line.pensize(2)
            line.setx(0)
            line.sety(y)
        else:
            exit

        line.forward(400)
        line.pendown()
        line.hideturtle()
        line.right(180)
        line.forward(800)

t = Turtle()
t.shape("square")
t.resizemode("user")
t.left(90)
t.shapesize(9.5,1)
t.showturtle()

Grid()
screen.update()
done()