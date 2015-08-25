# override explicity
class Parent(object):

    def function(self):
        print "Parent's function()"

class Children(Parent):

    def function(self):
        print "Children's function()"

parent = Parent()
son = Children()

parent.function()
son.function()
