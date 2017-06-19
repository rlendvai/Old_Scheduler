from turtle import *
import config
import time
import random
import itertools
import math

global screen
screen = Screen()
screen.tracer(50,0)

class Platform(Turtle):
    def __init__(self, x=0, y=0):
        Turtle.__init__(self, visible=False)
        self.platform_width_factor = config.platform_width_factor
        self.platform_height_factor = config.platform_height_factor
        self.elevator_pause = 0
        self.penup()
        self.pixel_height = config.platform_pixel_height * self.platform_height_factor
        self.pixel_width = config.platform_pixel_height * self.platform_width_factor
        self.setx(x + round((self.pixel_height * self.platform_width_factor / 2)))
        self.sety(y + round((self.pixel_height * self.platform_height_factor / 2)))
        self.x = x
        self.y = y
        self.speed(None)
        self.shape("square")
        self.resizemode("user")
        self.left(90)
        self.hideturtle()
        self.shapesize(self.platform_width_factor, self.platform_height_factor, 1)

    def move(self, distance):
        for i in range (distance):
            self.forward(1)
    def show(self):
        self.showturtle()

class Person(Turtle):
    def __init__(self, x=0, y=0, goal_floor = 0, current_floor = 0):
        Turtle.__init__(self, visible=False)
        #self._tracer(10)
        self.pixel_height = config.person_height
        self.pixel_width = config.person_width
        self.shape_size_unit_height = self.pixel_height / 21
        self.width_factor = .1 #width for shape stretch, not object
        self.shape_size_unit_width = self.pixel_width / 21
        self.height_factor = .5
        self.elevator_pause = 0
        self.penup()
        self.color("red")
        self.x = x
        self.y = y
        self.setx(x + round((self.pixel_height * self.width_factor / 2)))
        self.sety(y + round((self.pixel_height * self.height_factor / 2)))
        self.speed(None)
        self.shape("square")
        self.resizemode("user")
        self.left(90)
        self.hideturtle()
        self.shapesize(self.shape_size_unit_height, self.shape_size_unit_height, .1)
        self.goal_floor = goal_floor
        self.current_floor = current_floor
        self.writer = Turtle()
        self.writer.hideturtle()
    # return an array with key value pairs for x, y coordinates of lower left corner
    # and height and width of shape, in pixels
    def shape_info(self):
        return {'x' : self.x, 'y':self.y, 'height':self.height_factor, 'width':self.width_factor}
    def move(self, distance):
        for i in range(distance):
            self.forward(1)
    def show_floor(self):
        self.writer.penup()
        self.writer.setx(self.x)
        self.writer.sety(self.y)
        self.writer.right(90)
        self.writer.forward(10)
        self.writer.write(self.goal_floor, False,font=("Arial", 8, "normal"))
    def change_position_to(self,x, y):
        self.x = x
        self.y = y
        self.setx(x + round((self.shape_info()['width'] * self.width_factor / 2)))
        self.sety(y + round((self.shape_info()['height'] * self.height_factor / 2)))

class Lift():
    def __init__(self, Platform, capacity=0, floor_height = config.floor_height):
        self.platform = Platform
        self.floor_height = floor_height
        self.current_floor = 1
        if capacity == 0:
            self.capacity = round((Platform.pixel_width / config.slot_width))
        else:
            self.capacity = capacity
        self.slots = [Slot() for i in range (self.capacity)]
        for i in range (self.capacity):
            self.slots[i].x = Platform.x + (i * (config.slot_width)+2)
            self.slots[i].y = Platform.y + Platform.pixel_height
    # Takes a people Q and loads them onto the lift
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
    def unload(self):
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
    def move(self, distance):
        update_frames = config.update_frames
        for i in range (distance):
            for slot in self.slots:
                slot.move(1)
            self.platform.move(1)
        #screen.update()
    def move_floors(self, floors=1):
        self.move(round(self.floor_height*floors))
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
    def load(self, Person):
        if self.loaded == False:
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
            self.person.showturtle()
            self.person.show_floor()
    def move(self, distance):
        if self.isLoaded():
            self.person.move(distance)
    def width(self):
        return self.width

class Building():
    def __init__(self, num_lifts: object = 0, num_floors: object = 1) -> object:

        #do some math to distribute the lifts evenly in graphics
        lift_total_width = config.platform_pixel_width + 10
        #lower left corner of first lift
        lower_left = -(num_lifts/2*(lift_total_width))
        #each lift starts at first lift left corner plus a n lifts' width
        self.lifts = [Lift( Platform((lower_left + (i*(lift_total_width))),0)
                            ) for i in range (num_lifts)]
        self.num_floors = num_floors
        self.floor_height = config.floor_height
        self.floors = [Floor(self.floor_height * i) for i in range (num_floors)]

    def num_lifts(self):
        return len(self.lifts)
    def load_lift(self,lift_num, Q):
        self.lifts[lift_num].load(Q)
    def add_lift(self,Lift):
        self.lifts.append(Lift)
    def show(self):
        for lift in self.lifts:
            lift.show()
    def move_lift_gen(self, lift, num_floors):
        time_slice = 25 # in what fractions should the elevator be moved. Higher equals slower animation.
        for i in range (num_floors):
            for i in range (time_slice):
                lift.move_floors(1/time_slice)
                yield
            lift.unload()
            yield
        yield

    def move_lifts (self, num_floors):
        moves = []
        for lift in self.lifts:
            moves.append(self.move_lift_gen(lift, num_floors))
        interlaced = itertools.zip_longest(*moves)
        #interlaced = itertools.zip_longest(moves[0],moves[1], moves[2])
        for a, b, c in interlaced:
            pass

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







    #given a coordinate, places rows of slots on it, and returns number of slots not created
    def create_slots(self, x, y, num_seats, num_rows, num_slots):
        pass







class Floor(Turtle):
    def __init__(self, floorheight):
        Turtle.__init__(self, visible=False)
        self.penup()
        self.hideturtle()
        self.left(180)
        self.forward(300)
        self.right(90)
        self.forward(floorheight)
        self.right(90)
        self.color("dark green")
        self.pendown()
        self.hideturtle()
        self.forward(600)
        screen.update()






#returns the left lower coordinate of a turtle, assuming it is a cursor shape
def show_origin():
    myturtle = Turtle()
    myturtle.shape("circle")
    myturtle.resizemode("user")
    myturtle.shapesize(.1, .1)
    myturtle.color("red")
    myturtle.showturtle()
#lifts = [Platform(i*5,i*5) for i in range (5)]

