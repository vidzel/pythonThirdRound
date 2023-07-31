set_a = {'col', 'mex', 'bol'}
set_b = {'cr', 'bol'}

# Set union
set_c = set_a | set_b
print(set_c)

print(set_a.union(set_b))


# Intersection
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)


# Difference
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)


# Symmetric Difference
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)