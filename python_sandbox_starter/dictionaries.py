# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constrauctor
# person2 = dict(first_name='Sara', last_name='William')

# Get a value
    # LIKE person.first_name (in JS)
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person))
print(len(person2))

print(person)
print(person2)


# print(person2, type(person2))
# print(person)



### List of Dict ###
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kelvin', 'age': 25},
]
 
print(people[1])
print(people[1]['name'])