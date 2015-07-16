def loop(digit, inc):
    i = 0
    numbers = []
    while i < digit:
        numbers.append(i)
        i = i + inc
        print "Numbers now: ", numbers

digit = int(raw_input('> Enter digit for while loop: '))
inc = int(raw_input('> Enter incremental digit: '))
loop(digit, inc)
