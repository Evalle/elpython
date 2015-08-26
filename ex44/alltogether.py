# implicit, override, altered: all together

class Parent(object):

    def implicit(self):
        print "Parent implicit"

    def override(self):
        print "Parent override"

    def altered(self):
        print "Parent altered"

class Child(Parent):
    
    def override(self):
        print "Child Override"

    def altered(self):
        print "Before altered"
        super(Child, self).altered()
        print "After altered"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
