# ways to structure Python modules
# Topics: powers, import, random, while, other logic operators

# we usually write functions (and classes)
def raisePower(n):
    '''Raise the value of n to the cube power'''
    # validate that n is a numeric value
    if type(n)==int or type(n)==float: # we have == < <= > >= != 'and' 'in' 'or'
        return n**3 # ** means raise to the power
    else:
        return 'not a number'

# .. then later we invoke those functions (or methods of a class)
if __name__ == '__main__':
    # this is a very common syntax in Python
    # this is typically where we invoke the functions
    print( raisePower(4) ) # 64
    print( raisePower(-3) ) # -27

