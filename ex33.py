def loop(digit):
    i = 0
    numbers = []
    while i < digit:
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers

digit = int(raw_input('> '))
loop(digit)
