# Animal is-a object
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, ma,e):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a super
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee and has-a 120000 salary
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a Fish()
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
