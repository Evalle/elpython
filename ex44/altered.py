class Parent(object):
    
    def function(self):
        print "Parent"

class Child(Parent):

    def function(self):
        print "child"
        super(Child, self).function()
        print "Child"

dad = Parent()
son = Child()

dad.function()
son.function()
