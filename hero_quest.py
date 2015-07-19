from sys import exit
import string

# some variables

lives = 3
inventory = []

# this function is for hero's inventory
def invent():
    if len(inventory) == 0:
        print "Your inventory is empty now"
    else:
        for i in inventory:
            print "You have %r in you inventory" % i

# start the game
def start():
    print '''
    You're in the middle of the strange dark cave.
    you have %d lives now. Be careful my frined!

    TIP: If you want to check your inventory now
    you can just write 'inventory'

    You can see two doors.
    One in the left and another one in the right from you.
    Which one you will choose?
    ''' % lives
    choice = raw_input('> Choose your door (left or right): ')
    if "left" in choice:
        gold_room()
    elif "right" in choice:
        lab_room()
    elif "inventory" in choice:
        invent()
        start()
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
