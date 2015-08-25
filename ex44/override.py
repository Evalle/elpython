# override explicity
class Parent(object):

    def function(self):
        print "Parent's function()"

class Children(Parent):

    def function(self):
        print "Children's function()"

    def multiply(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num
        print first_num * second_num


parent = Parent()
son = Children()

parent.function()
son.function()
son.multiply(2,2)
