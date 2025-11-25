# Python respects scope for code blocks
# Everything that is not in a code block will always be 'global'
# This means we can safely assume everything can be imported elsewhere

a = 'in the global scope' # not indented, so it is in the global scope
b = None # we do not have to pre-declare b
def fnLocal():
    '''Anything we declare within a code block such as a function will be in a local scope'''
    global b # we declare an object and force it to exist in the global scope
    b = 'local scope (within a function)'
    print(b)
    # NB we may declare local functions that are objects belonging to a function
    def internalFn():
        b = 'other' # this is in it's own local scope

print(a)
print(b)
fnLocal()
print(b) # fails unless b was declared as global
