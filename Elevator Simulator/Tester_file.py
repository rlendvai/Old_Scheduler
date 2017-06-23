from turtle import *
from Elevators import *
import math
import itertools
global screen
screen = Screen()
screen.tracer(1,0)
import grid
import time

def shape_drawer():
    turtle=Turtle()
    s = Shape("compound")
    poly1 = ((0,0),(0,50),(50,50),(100,0))
    #poly1 = ((0,0),(0,5),(5,5),(0,0))
    s.addcomponent(poly1, "red", "blue")
    #poly2 = ((0,0),(10,-5),(-10,-5))
    #s.addcomponent(poly2, "blue", "red")

    turtle.screen.register_shape("myshape", s)
    turtle.shape("myshape")
    print(turtle.xcor(), turtle.ycor())


def ts (turtle, x, y, inner_width, width=100, height=100):

    turtle.setheading(0)
    turtle.hideturtle()
    turtle.begin_poly()
    turtle.begin_fill()
    turtle.color('red')


    turtle.setposition(x,y)
    turtle.setposition(width,y)
    turtle.setposition(width,height)
    turtle.setposition(x,height)
    turtle.setposition(x,y)

    turtle.setposition(x-inner_width, y-inner_width)

    turtle.setposition(width+inner_width,-y-inner_width)
    turtle.setposition(width+inner_width+x,height+inner_width)
    turtle.setposition(-inner_width,height+inner_width)
    turtle.setposition(x-inner_width,y-inner_width)

    turtle.end_fill()
    turtle.end_poly()
    p = turtle.get_poly()
    #register_shape('my_square', p)
    return p

def writer():
    w = Turtle()
    w.shape('square')
    w.shapesize(8,8)
    w.color('black')
    w.showturtle()
    w.write("100000000000", False, font=("arial", 8, "normal"))



#my_crowd = Q(200, bless=True, floor_start=1, floor_end=5)
#shape_drawer()

my_turtle = Turtle(visible=False)
screen.register_shape('holder', ts(my_turtle,0,0,10,10,100))
my_turtle.shape('holder')
my_turtle.penup()
my_turtle.showturtle()
my_turtle.forward(100)
my_turtle.rt(90)
my_turtle.forward(100)
#rect(my_turtle, 10, 100)
#t.shape('my_square')

#my_turtle.begin_fill()
''''''
#l = Lobby(0,0,30,100, my_crowd)
''''''
#grid.Grid()
done()