try:
    fh = open("test.txt", "r")
    fh.write("Some info is here\n")
except IOError:
    print "Error: can\'t find file or read data"
else:
    print "Written content to the file successfully"
    fh.close()
