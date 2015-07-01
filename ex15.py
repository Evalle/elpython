# import module 'argv' from 'sys'
from sys import argv 

# below ypu can find arguments that will be using in our script
script, filename = argv 

# variable 'txt' will be equal to contenat of 'filename' argument
txt = open(filename)

# Next we will print name of the file...     
print "Here's your file %r:" % filename

# ...and it's content. We are using here 'txt' variable with function read()
print txt.read()

# We asking for filename again
print "Type the filename again:"

# Here we using our raw_input which will be equal to 'file_again' variable
file_again = raw_input("> ")

# Here we're using open() fucntion again 
txt_again = open(file_again)

# ... and print out txt_again variable
print txt_again.read()

