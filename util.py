# we may collect some useful utilities into a module

def checkNumeric(n=0): # we expect a single positional argument. We may choose to provide default value
    '''Validate the incoming n is int or float
    If it is not, return zero'''
    if type(n) in (int, float):
        valid = True
    else:
        valid=False
    # we could have just returned in the logic above
    # if valid:
    #     return n
    # else:
    #     return 0
    # alternative syntax  [value_1] if [expression] else [value_2]
    return n if valid else 0

# what does Python call this module???
# dunder means leading and trailngi double underscore
# When run directly the module is ALWAYS named __main__
# when imported, python ALWAYS assignes __name__ to the module name ('util' in this case)
print(__name__) # NB anything with dunder belongs to Python

if __name__ == '__main__':
    ''' When the mdule is run directly, the following exercise code will run'''
    print( checkNumeric(33) )
    print( checkNumeric(-33) )
    print( checkNumeric(3.3) )
    print( checkNumeric('33') )
    print( checkNumeric(None) )
    print( checkNumeric() )   # the function arguent default value is used