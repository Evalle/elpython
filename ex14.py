from sys import argv

script, user_name, date = argv
prompt = '> '

print "Hi %s, I'm the %s script and today is %r" % (user_name, script, date)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Allright, so you said %r about liking me.
You live in %r. Not sure where it is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
