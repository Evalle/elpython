from sys import argv

script, filename = argv

print """
I'm going to erase %r please press 'Ctrl+C' 
if you don't want to do it and a 'Enter' 
if you do want it
""" % filename 

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"
target.write(line1 + "\n" + line2 + "\n" + line3)
print "And finally, we close it."
target.close()
