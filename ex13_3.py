# we need to combine raw_oinput with argv to make a script that gets more input from a user

from sys import argv 

script_name, second = argv
third = raw_input("Please write some information here: ")

print "Your script name is:", script_name
print "Your second argument is:", second
print "And your input is:", third
