# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# LIKE the previous lessons lists (except for this is unchangeable)

# Create a tuple
fruits = ('Apples', 'Oranges', 'Graphes')
# fruits2 = tuple(('Apples', 'Oranges', 'Graphes'))

# Single value needs trailing comma
fruits2 = ('apples', )

# print(fruits)
# print(fruits2, type(fruits2))

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get a value
# print(fruits2[0])


# print(len(fruits))




# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges' ,'Mongos'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Graphes')

# Remove from set
fruits_set.remove('Graphes')

# Clear set
fruits_set.clear()

# Delete set
del fruits_set


print(fruits_set)

