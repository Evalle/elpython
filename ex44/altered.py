# Altered before and after 

class Parent(object):
    
    def function(self):
        print "Parent function()"

class Child(Parent):
    
    def function(self):
        print "Child before parent altered"
        super(Child, self).function()
        print "Child after partent altered"

dad = Parent()
son = Child()

dad.function()
son.function()
        
