# working with dictionary and set
# dict is a collection containing any data type
# these collections are NOT ordinal - their members to not align to an ordered sequence
# there is nothing in Python to say the order of members of a dict or set should be in a particular order
# a dict is a collection of key:value pairs
# the key labels tend to be string literals
d = {'n':'Freda', 'type':'admin', 'current':True, 'age':42} # or dict()
print(d, type(d))
# dict is mutable
d['age'] += 1 # increment by 1
d['fave'] = 'Python'
# we cannot use numeric ordinality to access dict members
print(f"Name: {d['n']} Type:{d['type']} Age:{d['age']} Favourite:{d['fave']}")
# we may choose to iterate over all the key-value pairs in a dict
for (k, v) in d.items(): # d.values() and d.keys()
    print(k,v)

# a Set is a non ordinal, mutable collection of unique primitive values
my_set = {'Freda', 'Admin', 42, False, 'Freda', 4,4,4,3,3,2,1, 0} # curly braces may indicarw a set or a dict
# a set is mutable
my_set.remove('Freda')
my_set.add('Beth')
print(my_set, type(my_set))