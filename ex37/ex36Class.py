class Employee:
    'Common base class for all employees'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

evgeny = Employee("Evgeny", 5000)
evgeny.displayEmployee()
