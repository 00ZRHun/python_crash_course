 # JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict (dictionary)
    # json.stringify // json.parse (method in JavaScript)
user = json.loads(userJSON)

print(user, type(user))
print(user['first_name'])
 


# Python list
user = {"first_name": "John", "last_name": "Doe", "age": 30}

# Parse to json
userJSON = json.dumps(user)

print(userJSON, type(userJSON))

# /////////
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON, type(carJSON))

