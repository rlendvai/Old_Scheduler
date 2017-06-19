from Elevators import *
from Unit_tests import *
import random

DEBUG = True

if DEBUG:
    from Unit_tests import *

def main():
    #for n in range (5):    lifts[n].draw()
    # mylift2 = Platform(100,0)
    # mylift3 = Platform(200,0)
    # mylift1.move(100)
    # mylift2.move(100)
    # mylift3.move(100)
    #myperson = Person(0,0)
    #myperson.move(100)





    '''
    myplatform = Platform(0,0)
    myplatform2 = Platform(50,0)
    people_to_load = [Person(0,20), None, Person(0,20), Person(0,20), Person(0,20), Person(0,20), Person(0,20), None, None, Person(0,20)]
    mylift = Lift(myplatform)
    mylift2 = Lift(myplatform2)
    print (people_to_load)
    print (mylift.load(people_to_load))
    mylift.show()
    mylift2.show()
    mylift.move(80)
    mylift2.move(60)
    '''

floors = 7
lifts = 3
my_crowd = Q(30,bless=True, floor_start=2, floor_end=floors)
my_building = Building(lifts,floors)

my_building.load_lift(0,my_crowd)
my_building.load_lift(1,my_crowd)
my_building.load_lift(2,my_crowd)
my_building.show()
my_building.move_lifts(3)

#my_lobby = Lobby(0,0,200,100,my_crowd,100)
show_origin()
screen.update()
main()


done()