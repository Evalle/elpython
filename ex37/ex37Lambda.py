# example of using lambda functions in Python:
# normal function looks like this:

def f(x):
    return x**2

usr_input = int(raw_input("> "))

print f(usr_input)

# and lambda function:

g = lambda x: x**2

print g(8)
