# we may collect some useful utilities into a module

def checkNumeric(n):
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
    
if __name__ == '__main__':
    print( checkNumeric(33) )
    print( checkNumeric(-33) )
    print( checkNumeric(3.3) )
    print( checkNumeric('33') )
    print( checkNumeric(None) )
