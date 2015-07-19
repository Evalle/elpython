from sys import exit
import string

def start():
    print '''
    You're in the middle of the square room.
    You can see two doors.
    One in the left and another one in the right from you.
    Which one you will choose?
    '''
    choice = raw_input('> Choose your door (left or right): ')
    if "left" in choice:
        gold_room()
    elif "right" in choice:
        lab_room()
    else:
        print "Please choose your door"
        start()

def dead():
    exit(0)

def gold_room():
    print '''
    You're in the gold room
    '''
    dead()

def lab_room():
    print '''
    You're in the lab_room
    '''
    dead()

start()
