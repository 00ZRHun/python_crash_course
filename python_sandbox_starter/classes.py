# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def hasBirthday(self):
        self.age += 1

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'


# Extend class
# class Customer extends User: # the extends syntax in ES6(JS)
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'



# instantiate object
# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)

print(janet.greeting())

# print(brad, type(brad))
''' print(brad)
print(type(brad)) '''
# print(brad, '\n', type(brad))

# print(brad.name)
# print(brad.email)
# print(brad.age)

brad.hasBirthday()
print(brad.greeting())