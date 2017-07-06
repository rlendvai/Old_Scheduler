from turtle import *
from Elevators import *
import math
import itertools
global screen
screen = Screen()
screen.tracer(1,0)
import grid
import time

def err_duplication():
    screen.tracer(20, 0)
    t = Turtle()
    t2 = Turtle()
    t.color('green')
    t.setposition(0, 100)
    t.shape('square')
    t.showturtle()
    t2.color('black')
    t2.setposition(0, 95)
    t2.write("hahaha")
    screen.update()

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

    '''turtle.setposition(x-inner_width, y-inner_width)

    turtle.setposition(width+inner_width,-y-inner_width)
    turtle.setposition(width+inner_width+x,height+inner_width)
    turtle.setposition(-inner_width,height+inner_width)
    turtle.setposition(x-inner_width,y-inner_width)'''

    turtle.end_fill()
    turtle.end_poly()
    p = turtle.get_poly()
    #register_shape('my_square', p)
    return p

def writer():
    w = Turtle()
    w.write("100000000000", False, font=("arial", 10, "normal"))



#my_crowd = Q(200, bless=True, floor_start=1, floor_end=5)
#shape_drawer()

my_turtle = Turtle(visible=False)
screen.register_shape('holder', ts(my_turtle,0,0,10,10,100))
my_turtle.shape('holder')
my_turtle.penup()
my_turtle.showturtle()
writer()
''''''
#l = Lobby(0,0,30,100, my_crowd)
''''''
#grid.Grid()
done()