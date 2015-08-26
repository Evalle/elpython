# using super() with __init__

class Parent(object):
    variable = 5

class Child(Parent):
    pass

son = Child()

print son.variable
