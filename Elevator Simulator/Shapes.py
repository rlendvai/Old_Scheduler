from turtle import *
import math
import itertools
screen = Screen()
screen.tracer(1,0)
import grid
import time


def create_rect(x, y, width=10, height=100):

    turtle = Turtle()
    turtle.penup()
    turtle.setheading(0)
    turtle.hideturtle()
    turtle.begin_poly()
    #turtle.begin_fill()
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

    #turtle.end_fill()
    turtle.end_poly()
    p = turtle.get_poly()
    #register_shape('my_square', p)
    return p

def writer():
    w = Turtle()
    w.rt(90)
    w.fd(10)

    w.color('red')
    w.write("100000000000", False, font=("arial", 10, "normal"))

'''
t = Turtle(visible=False)
screen.register_shape('rectangle', create_rect(0,0))
t.shape('rectangle')
t.showturtle()
t.write("100000000000", False, font=("arial", 10, "normal"))
screen.update()
#writer()
done()'''