class MyStuff(object):
    
    def __init__(self):
        self.variable = "some text"

    def apples(self):
        print "Some apples here"

x = MyStuff()

print x.variable
x.apples()
