# ways to structure Python modules
# we try to import libraries at the top of a module
import random # random is one the many built in libraries


# Topics: powers, import, random, while, other logic operators

# we usually write functions (and classes)
def raisePower(n):
    '''Raise the value of n to the cube power'''
    # validate that n is a numeric value
    if type(n)==int or type(n)==float: # we have == < <= > >= != 'and' 'in' 'or'
        return n**3 # ** means raise to the power
    else:
        return 'not a number'
    
def checkIfPrime(n):
    '''Check to see if n is a prime number between 0 an 100'''
    # here we declare a variable which is only visible within this function
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    if n in primes:
        return f'{n} is a prime number'
    else:
        return f'{n} is not a prime number between 0 an 100'

def r():
    '''return a random integer 0-10'''
    i = random.randint(0,10)
    return i


# .. then later we invoke those functions (or methods of a class)
if __name__ == '__main__':
    # this is a very common syntax in Python
    # this is typically where we invoke the functions
    print( raisePower(4) ) # 64
    print( raisePower(-3) ) # -27
    print( checkIfPrime(3) )
    print( checkIfPrime(30) )
    print( checkIfPrime(29) )

