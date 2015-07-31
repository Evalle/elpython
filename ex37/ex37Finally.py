try:
    fh = open("test.txt", "r")
    try:
        fh.write("some info\n")
    finally:
        print "Going to close the file"
        fh.close()
except IOError:
    print "Error: can\'t find file or read data"
