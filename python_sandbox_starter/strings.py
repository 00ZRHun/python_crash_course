# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Zu Rong'
age = '21'

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
# print('Hello, my name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')



### String Methods ###

s = 'hello world'
# s = '123'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# get length
print(len(s))

# Replace
print(s.replace('hello', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Start with
print(s.startswith('hello'))

# End with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())