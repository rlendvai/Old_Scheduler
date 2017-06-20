from Elevators import *
from Unit_tests import *
import random
import grid

DEBUG = True

if DEBUG:
    from Unit_tests import *

def main():
    screen.tracer(50,0)
    floors = 10
    lifts = 3
    my_crowd = Q(200,bless=True, floor_start=1, floor_end=floors)
    my_building = Building(num_lifts = lifts, num_floors = floors)

    for i in range (lifts):
        my_building.load_lift(i,my_crowd)
    my_building.show()
    my_building.move_lifts(floors-1)
    #my_lobby = Lobby(0,0,200,100,my_crowd,100)
    screen.update()


grid.Grid()
main()

done()