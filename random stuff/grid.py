from turtle import *


class Grid():
    def __init__(self):
        g = Turtle(visible=False)
        g.hideturtle()
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
        line.screen.tracer(0,0)
        line.speed(None)
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

        line.forward(1000)
        line.pendown()
        line.hideturtle()
        line.right(180)
        line.forward(2000)
        line.hideturtle()
