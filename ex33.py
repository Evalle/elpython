i = 0
numbers = []

def loop(digit):
    i = 0
    numbers = []
    while i < digit:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print "The numbers: ", numbers

#for num in numbers:
#    print num


digit = int(raw_input('> '))
loop(digit)
