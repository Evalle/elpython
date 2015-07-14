print "You enter a dark room with three doors. What door will you choose? Door #1, Door #2 or Door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your leg off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding resolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "You enter a dark room, door immideatly closing behind you. You heard someone's creepy voice. What should you do?"
    print "1. You trying to open door behind you."
    print "2. You striking a match."
    print "3. You screaming."
    do = raw_input("> ")

    if do == "1":
        print "Creature in the dark eats you. Good job!"
    elif do == "2":
        print "Creature in the dark scream of fear, and immediatly jump on you. You die. Good job!"
    elif do == "3":
        print "Creature in the dark running in fear. It broke the door. Your free now! Good job!"
    else:
        print "You're waiting too long, creature in the dark screaming. Last thing that you heard in your life was this scream"
else:
    print "You stumble around and fall on a knife and die. Good job!"
