set_countries = {'cr', 'mx', 'arg'}

# size
size = len(set_countries)
print(size)

# locate a single element in a set
print('cr' in set_countries)
print('usa' in set_countries)

# adding 
set_countries.add('per')
print(set_countries)

# update
set_countries.update({'nic', 'usa', 'pe'})
print(set_countries)

# remove
set_countries.remove('per')
print(set_countries)
#set_countries.remove('ch') it gives an error in the element does not exist

# dicard
set_countries.discard('ch')

# clear all the set
set_countries.clear()
print(len(set_countries))
print(set_countries)