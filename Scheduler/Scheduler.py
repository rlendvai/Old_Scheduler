from turtle import *

import names
import pickle
import arrow
from dateutil import tz



class Appointment():
    def __init__(self, duration):
        self.patient = Patient()
        self.duration = 30



class Patient():
    def __init__(self):
        self.name = names.get_full_name()

class Slot():
    def __init__(self, begin_time, length):
        self.appointment = None
        self.type = "General"
        self.begin_time = begin_time
        self.fill(Appointment(30))


    def fill(self, appointment):
        #assert self.appointment == None, "Trying to fill already filled slot!"
        if self.appointment == None:
            self.appointment = appointment
            return True
        else:
            sys.exit("You can not fill an already filled slot!")
    def unfill(self):
        self.appointment = None


    def filled_string(self):

        return_string = self.begin_time.format('HH:mma') + ' '

        if self.appointment != None:
            return_string = return_string + self.appointment.patient.name
        else:
            return_string = return_string + '    <FREE>    '

        return return_string

    def filled_status(self):
        if self.appointment == None:
            return False
        else:
            return True

    def __lt__(self, other):
        pass



class Day():
    def __init__ (self, arrow_day, total_slots, length):
        self.slots = []
        self.begin_time = arrow_day
        for i in range (total_slots):
            self.slots.append(
                Slot(self.begin_time.shift(minutes=(30*i)), length)
                            )

    def show(self):
        print(emphasize(self.begin_time.format('dddd')))

        for i in range(len(self.slots)):
            print(self.slots[i].filled_string())

    def add_appointment (self, begin_time, appointment):
        slot = self.slots[slot_no]
        return slot.fill(appointment)

    def cancel_appointment(self, slot):

        self.slots[slot].unfill()

    #def filled_slots(self):



class Schedule ():
    def __init__(self, num_days = 1, num_slots = 4, duration = 30):
        self.start = arrow.get('2017, 07, 01, 09am, 00', 'YYYY, MM, DD, HHa, mm')
        self.days = []
        self.initialize(num_days, num_slots)
        self.duration = duration


    def initialize(self, num_days, num_slots):

        for i in range (num_days):
            self.days.append(Day(self.start.shift(days=i), num_slots, 30))

    def show(self):
        for day in self.days:
            day.show()
    def cancel_appointment(self, day, slot):

        self.days[day-1].cancel_appointment(slot-1)

    def waitlist(self):
        waitlist=[]
        # for day in self.days:





def emphasize(string):
    emphasis = "*******"
    string = string.upper()
    new_string = emphasis + " " + string + " " + emphasis
    return new_string

def main():

    FRESH = False
    DAYS = 2
    SLOTS = 4
    DURATION = 30

    if FRESH:
        myschedule = Schedule(DAYS, SLOTS, DURATION)
    else:
        fh = open("schedule.obj", "rb")
        myschedule = pickle.load(fh)


    myschedule.show()
    myschedule.cancel_appointment(2,1)
    myschedule.cancel_appointment(2,4)
    myschedule.show()

    a= myschedule.days[0].slots[0].begin_time.datetime
    b=myschedule.days[0].slots[1].begin_time.datetime

    print(a<=b)


    fh = open("schedule.obj", "wb")
    pickle.dump(myschedule, fh)
    fh.close()



main()

