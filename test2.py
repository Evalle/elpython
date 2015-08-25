class Parent(object):

    def function(self):
        print "Parent's function()"

class Child(Parent):
    pass

dad = Parent()
child = Child()

dad.function()
child.function()
