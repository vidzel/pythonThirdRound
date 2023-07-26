set_countries = {'cr', 'mx', 'arg'}
print(type(set_countries))
print(set_countries )

set_numbers = {1,2,2,4,6,888}
print(set_numbers)

set_types = {2, 'hello', True, 39.48}
print(set_types)

# Creating a set fron another data structure like a string

set_from_string = set('Hellooo!')
print(set_from_string)

# From a tuple
set_from_tuple = set(('ab', 'cd', 'ab', 'zm'))
print(set_from_tuple)

# From a list
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

# From a set to a list in order to pick unique values
unique_nums = list(set_numbers)
print(unique_nums)