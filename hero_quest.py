from sys import exit
import string

lives = 3
inventory = []

# this function is for hero's inventory checking
def check_invent():
    if len(inventory) == 0:
        print '''
    >>> Your inventory is empty <<<
    '''
    else:
        for i in inventory:
            print "You have the %r in you inventory" % i

# this function is for hero's lives checking
def check_lives():
    global lives
    if lives == 1:
        print '''
        >>> You have only 1 live left, be careful! <<<
        '''
    else:
        print '''
        >>> You have %d lives <<<
        ''' % lives

def dead():
    print '''
    >>> You have no lives left you're dead! <<<
    '''
    exit(0)

def tip1():
    print '''
    TIP: If you want to check your inventory now
    you can just write 'inventory'
    '''

def tip2():
    print '''
    TIP: To check the status of you lives now
    you can just write 'lives'
    '''

def damage():
    global lives
    lives = lives - 1
    return lives

tip1()
tip2()
# start the game
def start():
    global lives

    if lives == 0:
        dead()
    else:

        print '''
    You're in the middle of the strange dark cave.
    You can see two doors.
    One in the left and another in the right from you.
    Which one you will choose?
    '''

        choice = raw_input('> Choose your door (left or right): ')

        if "left" in choice:
            gold_room()
        elif "right" in choice:
            lab_room()
        elif "inventory" in choice:
            check_invent()
            start()
        elif "lives" in choice:
            check_lives()
            start()
        elif "exit" in choice:
            exit(0)
        else:
            print "Please choose your door"
            start()

def gold_room():

    if lives == 0:
        dead()
    else:
        print '''
        You're in the gold room.
        It's full of gold coins,
        In front of you there are two big statues.
        You can feel that they're watching you.
        One of the statues has a sword.
        Another one has a shield.
        What will you do?
        '''
        choice = raw_input("> Make your choice: ")

        if "coin" in choice:
            print '''
            You feel that the floor is going down from over your feet.
            You falling down into darkness...
            '''
            damage()
            start()
        elif "take" and "sword" in choice:
            inventory.append('sword')
            print '''
            Now you have the sword, good job!
            '''
            gold_room()
        elif "take" and "shield" in choice:
            inventory.append('shield')
            print '''
            Now you have the shiled, good job!
            '''
            gold_room()
        elif "inventory" in choice:
            check_invent()
            gold_room()
        elif "lives" in choice:
            check_lives()
            gold_room()
        elif "exit" in choice:
            exit(0)

def lab_room():

    if lives == 0:
        dead()
    else:
        print '''
    You're in the Great Sorcerer's labaratory.
    You see a lot of interesting stuff here:
    Bat wings, skulls, and old books with strange sparkly names on them.
    On the big wood table you can see three poitions:
    A blue one.
    A green one.
    And a red one.
    What will you do?
    '''
        choice = raw_input('> Make your choice: ')
        if "drink" in choice:
            print '''
    You feel a fire inside you.
    You last thought in this life was:
    "This is was a not good idea to drink
    a potion in Sorcerer's room"
        '''
            damage()
            start()
        elif "take" in choice:
            print '''
    You can hear the steps behind you.
    You turned around immediatly and last thing
    that you can saw was the angry old mans' face
        '''
            damage()
            start()
        elif "inventory" in choice:
            check_invent()
            lab_room()
        elif "lives" in choice:
            check_lives()
            lab_room()
        elif "exit" in choice:
            exit(0)
start()
