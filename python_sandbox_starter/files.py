# Python has functions for creating, reading, updating, and deleting files.

# Open a file
    # Mode = w(write) // a(append)
myFile = open('myFile.txt', 'w')

# Close file
# myFile.close()

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

''' print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode) '''

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)     # 100 character
print(text)