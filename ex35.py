from sys import exit

def start():
    print '''
    You are in the dark room.
    There is a door to your right and left.
    print "Which one do you take?
    '''
    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        magic_lab()
    else:
        dead("You stumble around the room until you starve.")

def dead(why):
    print why, "Good job!"
    exit(0)

def cthulhu_room():
    print '''
    Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    print "Do you flee for your life or eat your head?
    '''
    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def bear_room():
    print '''
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    '''
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        # true and not false == true
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        # true and False ? 
        elif choice == "taunt bear" and bear_moved:
            print "This is not a good idea to taunt bear once again!"
        elif choice == "taunt bera" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def magic_lab():
    print '''
    This is Great sorcerer's magic labarotory.
    You can see three poition on the table.
    Green, blue and red one. 
    What will you do?
    '''
    choice = raw_input("> ")
    if 'drink' and 'blue' in choice:
        cthulhu_room()
    elif 'drink' and 'green' in choice:
        dead("It's not a good idea to drink something in Sorcerer's lab!")
    elif 'drink' and 'red' in choice:
        gold_room()    
    else:
        print "I don't understand you"
        magic_lab()

def gold_room():
    print '''
    This room is full of gold. How much do you take?
    '''

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

start()
