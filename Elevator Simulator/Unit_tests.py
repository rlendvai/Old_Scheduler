from Elevators import *



def slot_unit():
    myslot = Slot(x=0)
    myperson = Person()
    assert myslot.isLoaded() is False, "New slot should be empty."
    myslot.load(myperson)
    assert myslot.isLoaded() is True, "An empty slot should be load-able."
    assert myslot.load(myperson) is False, "Loading should fail when attempting to load a full slot."

def Q_unit():
    persons = 3

    crowd = Q(persons)
    assert crowd.headcount() == 3, "Q headcount test failed"

def lift_unit():

    my_Q = Q(10)
    myPlatform = Platform()
    mylift = Lift(myPlatform, 6)
    resulting_Q = mylift.load(my_Q)
    assert resulting_Q.headcount() == 4 , "Lift load test failed"
    resulting_Q = mylift.load(resulting_Q)
    assert resulting_Q.headcount() == 4, "Lift load test failed."

    my_Q = Q(3)
    mylift = Lift(myPlatform,10)
    resulting_Q = mylift.load(my_Q)
    assert resulting_Q.headcount() == 0 , "Lift load test failed"
    print (my_Q)



slot_unit()
Q_unit()
lift_unit()