# dictionaries:
# create a mapping of state to abbrevation
divider = '-' * 10

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'Califorina': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
}

# create a basic set of states ans some cities in them

cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print divider
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states 
print divider
print "Michigan's abbrevation is: ", states['Michigan']
print "Florida's abbrevation is: ", states['Florida']

# do it by using the state then cities dict
print divider
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbrevation
print divider
for state, abbrev in states.items():
    print "%s is abbrevated %s" % (state, abbrev)


