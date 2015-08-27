from other import Other

class Child(object):
    
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override"

    def altered(self):
        print "CHILD altered before other"
        self.other.altered()
        print "CHILD altered after other"

son = Child()

son.implicit()
son.override()
son.altered()
