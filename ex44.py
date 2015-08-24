# Override Explicity

class Parent(object):

    def function(self):
        print "Parent function()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.function()
son.function()
