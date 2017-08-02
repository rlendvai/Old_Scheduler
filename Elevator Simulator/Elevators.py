from turtle import *
import config
import random
import itertools
import math
import time
from Shapes import *

global screen
screen = Screen()
screen.tracer(0,1)
global writer_t
writer_t = Turtle()

class Platform(Turtle):
    def __init__(self, x=0, y=0):
        Turtle.__init__(self, visible=False)
        self.pixel_height = config.platform_pixel_height
        self.pixel_width = config.platform_pixel_width
        self.width_factor = self.pixel_width / config.SHAPE_LENGTH
        self.height_factor = self.pixel_height / config.SHAPE_LENGTH
        self.elevator_pause = 0
        self.penup()
        self.setx(x + round((self.pixel_width / 2)))
        self.sety(y + round((self.pixel_height / 2)))
        self.x = x
        self.y = y
        self.speed(None)
        self.shape("square")
        self.resizemode("user")
        self.left(90)
        self.hideturtle()
        self.shapesize(self.width_factor, self.height_factor)

    def shape_info(self):
        return {'x' : self.x, 'y':self.y, 'height':self.pixel_height, 'width':self.pixel_width}
    def move(self, distance):
        for i in range (distance):
            self.forward(1)
    def show(self):
        #print('platform: ', self.xcor(), ',', self.ycor())
        self.showturtle()

class Person(Turtle):
    def __init__(self, x=0, y=0, goal_floor = 0, current_floor = 0):
        Turtle.__init__(self, visible=False)
        self.pixel_height = config.person_height
        self.pixel_width = config.person_width
        self.height_factor = self.pixel_height / config.SHAPE_LENGTH
        self.width_factor = self.pixel_width / config.SHAPE_LENGTH  #width for shape stretch, not object
        self.elevator_pause = 0
        self.penup()
        self.color("red")
        self.x = x
        self.y = y
        self.setx(x + round((self.pixel_width / 2)))
        self.sety(y + round((self.pixel_height / 2)))
        self.speed(None)
        screen.register_shape('rectangle', create_rect(0,0, 20, 20))
        self.shape('rectangle')
        self.resizemode("user")
        self.left(90)
        self.hideturtle()
        #print("person width factor: ", self.width_factor)
        self.shapesize(self.width_factor, self.height_factor, 0)
        self.goal_floor = goal_floor
        self.current_floor = current_floor
        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.stamp_id = None
    # return an array with key value pairs for x, y coordinates of lower left corner
    # and height and width of shape, in pixels
    def shape_info(self):
        return {'x' : self.x, 'y':self.y, 'height':self.pixel_height, 'width':self.pixel_width}
    def show(self, goal_position = 'inside'):

        self.penup()
        self.showturtle()
        #screen.update()
        #self.writer.setposition(self.shape_info()['x']+5, self.shape_info()['y'])
        #self.writer.write(self.goal_floor, True, font=("Arial",8,"normal"))
        #screen.update()

    def move(self, distance):
        self.penup()
        for i in range(distance):
            self.forward(1)
    def show_floor(self, goal_position = 'inside'):

        if goal_position == 'inside':
            self.pendown()
            self.writer.color('black')
            self.writer.setx(self.x)
            self.writer.sety(self.y)
            self.writer.left(90)
            self.writer.forward(2)
            self.color('black')
            self.write(self.goal_floor, False, align = 'center' ,font=("Arial",8,"normal"))
            self.color('red')
            #self.writer.write("1000", True, font=("Arial",8,"normal"))
            #self.writer.forward(5)
    def change_position_to(self,x, y):
        self.x = x
        self.y = y
        #print("moving person'x to: ", (x + round((self.shape_info()['width'] / 2))))
        self.setx(x + round((self.shape_info()['width'] / 2)))
        self.sety(y + round((self.shape_info()['height'] / 2)))
        #show_position(x,y)
        '''newt=Turtle()
        newt.setx(-305)
        newt.pendown()
        newt.left(90)
        newt.forward(100)
        newt.right(90)
        newt.forward(200)
        newt.left(90)
        newt.forward(100)'''

class Lift():
    def __init__(self, Platform, floor_height = config.floor_height, slot_width = config.slot_width, gap_width = config.slot_gap_width):
        self.platform = Platform
        self.floor_height = floor_height
        self.current_floor = 1
        self.capacity = math.floor(Platform.shape_info()['width']/ (slot_width + gap_width))
        self.slot_width = slot_width
        self.slots = [Slot() for i in range (self.capacity)]
        self.place_slots(gap_width) # there should be a 2 pixel gap between slots

    # Takes a people Q and loads them onto the lift
    #gap is the gap that should be left between adjacent slots
    def place_slots(self, gap):
        for i, slot in enumerate(self.slots):
            p_x = self.platform.shape_info()['x']
            p_y = self.platform.shape_info()['y']
            slot.change_position(p_x + (i * (self.slot_width + gap)),
                                 p_y + self.platform.shape_info()['height'])
    def load(self, Q):
        people = Q.people
        #Try each slot. Load it if it's empty. Keep going until you run out of slots or people.
        for slot in self.slots:
            if slot.isLoaded() == False:
                next_person = None
                while(next_person == None and len(people)>0):
                    next_person = people.pop()
                #need to check if next_person is None b/c we may have exited for loop even if no one was found
                if next_person != None:
                    slot.load(next_person)
        Q.people = people
        return Q
    def unload(self, pause = .2):
        for slot in self.slots:
            if slot.isLoaded():
                if slot.person.goal_floor == round(self.current_floor):
                    slot.unload()
    def width(self):
        return self.platform.pixel_width

    def show(self):
        for slot in self.slots:
            slot.show()
        self.platform.show()

    #moves the lift and the people in it
    def move_pixels(self, distance):
        update_frames = config.update_frames
        #for i in range (distance):
        '''for slot in self.slots:
                slot.move(1)
            self.platform.move(1)'''
        for slot in self.slots:
           slot.move(distance)
        self.platform.move(distance)
        #update screen after platform moves
        #screen.update()
    def move_floors(self, floors=1):
        self.move_pixels(round(self.floor_height * floors))
        self.current_floor = self.current_floor + floors
        return self.current_floor


        #for slot in self.slots:
         #   slot.person._tracer(1)



class Q():
    def __init__(self, people = 0, bless = False, floor_start=0, floor_end=0):
        if bless == True:
            self.people = [Person(goal_floor=random.randint(floor_start,floor_end)) for i in range(people)]
        else:
            self.people = [Person() for i in range (people)]
    def headcount(self):
        return len(self.people)
    def people(self):
        return self.people


class Slot():
    def __init__(self, x=0, y=0, loaded = False):
        self.x = x
        self.y = y
        self.width = config.slot_width
        self.loaded = loaded
        self.person = None

    def shape_info(self):
        return {'x': self.x, 'y': self.y, 'height': None, 'width': self.width}

    def load(self, Person):
        if self.loaded == False:
            assert Person.shape_info()['width'] <= self.width , "Person wider than slot!"
            self.person = Person
            self.person.change_position_to((self.x+1), self.y+1)
            self.loaded = True
            return True
        else:
            return False
    def unload(self):
        if self.loaded == True:
            self.person = None
            self.loaded = False
    def isLoaded(self):
        return self.loaded
    def show(self):
        if self.isLoaded():
            self.person.show()
            self.person.getscreen().update()
            #screen.update()
            self.person.show_floor()
            #screen.update()

    def move(self, distance):
        if self.isLoaded():
            self.person.move(distance)
    def change_position(self, x, y):
        self.x = x
        self.y = y
        if self.loaded:
            self.person.change_position_to(self.x, self.y)

    def width(self):
        return self.width


class Building():
    def __init__(self, x=0, y=0, num_lifts =1 , num_floors = 3):


        self.num_floors = num_floors
        self.floor_height = config.floor_height
        self.floors = [Floor(self.floor_height * i) for i in range (num_floors)]
        self.x = x
        self.y = y
        self.lifts = []
        self.create_lifts(num_lifts)
        self.show()

    def num_lifts(self):
        return len(self.lifts)

    def load_lift(self,lift_num, Q):
        self.lifts[lift_num].load(Q)

    def create_lifts(self, num_lifts):
        platform_width = config.platform_pixel_width
        gap_width = config.lift_gap_width
        total_building_width = (num_lifts * platform_width) + ((num_lifts-1) * gap_width)
        left_corner = -(total_building_width / 2)

        for i in range (num_lifts):
            x = left_corner + (i * (platform_width + gap_width))
            self.lifts.append(Lift(Platform(x, -(config.platform_pixel_height))))

    def show(self):
        for lift in self.lifts:
            lift.show()

    def move_lift_gen(self, lift, num_floors):
        time_slice = 25 # in what fractions should the elevator be moved. Higher equals slower animation.
        for r in range (num_floors):
            for i in range (time_slice):
                lift.move_floors(1/time_slice)
                yield
            lift.unload()
            print("unloading floor: ", r)
            yield

        yield

    def move_lifts (self, num_floors):

        time_slice = 25

        '''for i in range (num_floors):
            for t in range (time_slice):
                for lift in self.lifts:
                    lift.move_floors(1/time_slice)
                    if t == time_slice - 1:
                        lift.unload()
                screen.update()'''

        moves = []


        for lift in self.lifts:
            moves.append(self.move_lift_gen(lift, num_floors))

            interlaced = itertools.zip_longest(*moves)

        for i in interlaced:
            screen.update()

        '''for a, b, c in interlaced:
            pass'''

class Lobby:
    def __init__(self, x, y, lobby_height, lobby_width, Q=None, capacity=100):
        self.peopleQ = Q
        self.capacity = capacity
        self.slot_width = config.slot_width
        self.row_height = config.person_height + 2
        self.num_seats_in_row = math.floor(lobby_width / self.slot_width)
        self.num_rows = math.floor(lobby_height / self.row_height)
        self.slots = []
        self.x = x
        self.y = y
        self.add_all_slots()
        self.lobby_height = lobby_height
        self.lobby_width = lobby_width

    # try to create a number of slots over available seats, return the number of slots not created
    def add_slots_to_row(self, x, y):

        slots = [Slot((x+(i*self.slot_width)),y) for i in range (self.num_seats_in_row)]
        for slot in slots:
            slot.load(Person())
            slot.show()
        #num of slots not created
        return slots
    def add_all_slots(self):
        for i in range (self.num_rows):
            self.slots.append(self.add_slots_to_row(self.x, self.y + (i*self.row_height)))
    def show(self):
        t=Turtle()
        t.hideturtle()
        t.penup()
        t.setx(self.x)
        t.sety(self.y)
        t.pendown()
        t.forward(self.slot_width*self.num_seats_in_row)


    #given a coordinate, places rows of slots on it, and returns number of slots not created
    def create_slots(self, x, y, num_seats, num_rows, num_slots):
        pass







class Floor(Turtle):
    def __init__(self, floorheight):
        Turtle.__init__(self, visible=False)
        self.penup()
        self.hideturtle()
        self.left(180)
        self.forward(500)
        self.right(90)
        self.forward(floorheight)
        self.right(90)
        self.color("dark green")
        self.pendown()
        self.hideturtle()
        self.forward(1000)
        screen.update()






#returns the left lower coordinate of a turtle, assuming it is a cursor shape
def show_position(x, y):
    myturtle = Turtle()
    myturtle.penup()
    myturtle.setx(x)
    myturtle.sety(y)
    myturtle.shape("circle")
    myturtle.resizemode("user")
    myturtle.shapesize(.1, .1)
    myturtle.color("red")
    myturtle.showturtle()
    myturtle.penup()
#lifts = [Platform(i*5,i*5) for i in range (5)]

