# here we write functions
def fnA(x): # we may choose to pass in arguments
    '''we often provide a docstring to explain a function'''
    print(f'value of x is {x} of type {type(x)}')

def askUser(prompt):
    '''show the user a prompt and invite them to respond by typing'''
    # the code will pause for input and only continue when the user presses ENTER
    u = input('please type something: ')
    return u # we my choose to return something from a function



# we can invoke any function as often as we like
fnA(4)
fnA(None)
fnA('wibble')
fnA(False)
fnA( [4,3,2] )
fnA( (4,7,-1) )