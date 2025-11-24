# here we write functions
def fnA(x): # we may choose to pass in arguments
    '''we often provide a docstring to explain a function'''
    print(f'value of x is {x} of type {type(x)}')

# careful any type hints are ONLY used by code help tools
# type hints are completely ignored by Python
def demoFn()->int: # a code hint
    return "not an integer"

def askUser(prompt):
    '''show the user a prompt and invite them to respond by typing'''
    # the code will pause for input and only continue when the user presses ENTER
    u = input(prompt)
    # respond differently depending on the nature of the input
    if u.isnumeric(): # checks to see if the string contains ONLY digits (not . or -)
        u = int(u) # cast the string to an integer
    elif u == '': # else if
        u = None # convert an emtpy string to None 
    else:
        pass # useful if we may come back and change this code       

    return u # we my choose to return something from a function


# we can invoke any function as often as we like
fnA(4)
fnA(None)
fnA('wibble')
fnA(False)
fnA( [4,3,2] )
fnA( (4,7,-1) )
response = askUser('Enter value: ')

print(response, type(response)) # the result of input() is ALWAYS a string