# here is a comment (we use the # sign for comments)
# variables and identifiers may use letters, numbers and underscore
# ...don't start with a digit
# we do not terminate statements with a semi colon ;
# Python is a loosely typed language. There are tyoes but theres no rigour
a = 3      # here we have an integer
b = 7.5    # this is a float
# any variable may have a different data type assgined at any time
a = a/2    # a is no longer an integer
print(a, type(a), b, type(b))
# other simple data types
w = True # or False these are Boolean
x = None # the none-type represents the absence of anything else


# there are several collection data-types in Python
# string, list, tuple, set, dict
s = "Welcome to the Python programming language" # this is an ordinal immutable colletion of characters
print(s[9]) # 'o'
# slicing is common cross all ordinal collections
print( s[4:21:2] ) # slicing is always start:stop-before:step, with sensible defaults
# we can use connvenient print formatting to nicely output our print
print(f"We have {b}, also {w} and {s[11:33]}") # NB this is a string builder - the string is immutable
# you my come across this alternative string formtting syntax
print("We have {}, also {} and {}".format(b,w,s[11:33])) # NB this is a string builder - the string is immutable

# List and Tuple
# a list is an ordinal mutable collection of any data type
l = list( (4,7,7,9,4,2) ) # here we explicitly create a list (from a tuple)
k = [4,7,2,8,1,22] # this is more common
# lists are mutable so we may choose to alster their contents
l[0] = 'changed'
k[3] = None
# other list mutations
k.insert(3, 'added')
k.append(l) # we may have any data type within our list
print(l, k, type(l))
# mini challenge: 
print( k[7][0][2] ) # we may access members within members within members of a collection

# strings and quotes
# Python does not care which quote marks you use
d = 'hello'
e = "double \nhello\tfollowed by tab" # we may choose to encode whitespace
# tripple quotes let us incluse whitespace (tabs, new lines etc)
f = '''this is cool
is it                   time for break???'''
g = """still 
cool"""
print(d, e, f, g)

# Operators
# + - / * are easy
# // for modulo dovision
# % for remainder after division

m = 5
n = 2
print(m/n, m//n, m%n) # 2.5, 2, 1

# tuples
t = tuple(l) # take all the members of the list 'l' and populate a tuple
# a tuple is an ordinal immutable collection of any data type
t = (4,3,2,1)
print(t, type(t), t[0:3]) # we cannot insert, append or change an existing tuple (imutable)

# list and tuple are very similar except a list is mutable
# We may iterate over any oordinal collection
for i in t: # start at the member 0 and keep going until we run out of members
    print(i)

# Code blocks are declared using a colon and indentation
# the colon is the start of a code block
# the code block continues until the indentation ends