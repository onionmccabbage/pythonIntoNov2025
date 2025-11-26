# map lets us apply a function to every value in a collection
# filter lets us compare every value in a colection using a function

def makeSquare(n):
    '''return the square of the given value'''
    return n**2

def checkEven(n):
    '''check to see if the given value is an even integer'''
    isInt = False
    if type(n)==int and (n/2 == int(n/2)):
        isInt=True
    return isInt

def main():
    '''It is common practice to have a function called main'''
    # use map (make a tuple or a list)
    # NB be careful we do not call the function, we merely refer to it
    s = tuple(map(makeSquare, range(1,11))) # NB any collection will do - a range, a generator, a list a tuple...
    print( s )
    # use filter
    f = list(filter(checkEven, range(0,11)))
    print(f) # a filter object


if __name__ == '__main__':
    '''exercise the code'''
    main()
