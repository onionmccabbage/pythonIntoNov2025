# the range object and also genertors

r = range(10**6,-10**6,-3) # range is always start, stop-before,step with sensible defaults
# Range is particularly efficient, since the values only exist on demand

print(r, type(r))

for i in r:
    pass
    j = i*i
    # print(i) # I/O bound - all input and all output is nessecarily s-l-o-w

# a range is often used as a convenience when iterating
for _ in range(0,11):
    print(_)

# generators
# imagine we need a bunch of square numbers
squares = (i*i for i in range(0,11))
for s in squares:
    print(f'The next square numer is {s}')

# we may even call functionality into our generator
def fiveFactor(n):
    if n//5 == int(n/5):
        return n
    else:
        return None

fives = (fiveFactor(_) for _ in range(-50, 51)) # this is a generator, not a tuple
print(fives, type(fives))
for _ in fives:
    print(_, end=', ') # we may choose to override the default new-line

# we can include the functionality within the generator
evens = ( _ for (_//2==int(_/2) in range(0,11))

# for _ in evens:
#     print(_)

