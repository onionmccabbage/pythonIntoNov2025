# we may choose to write our code across several modules
import datetime # we have access to everything in the datetime library
# alternatively we may just import the bits we need
from datetime import datetime # we now have just teh datetime feature from the datetime library
# we can import from our own modules
import util # we have it all
# or
from util import checkNumeric

# there is never a problem to including functions within a main module
def today():
    '''provide a nicely formtted date-time string'''
    # if we imported the entire library we must fully qualify our feature calls
    # now = datetime.datetime.date( datetime.datetime.today() )
    now = datetime.date( datetime.today() ) # just calling the datetime feature
    return now

def main():
    '''By convention this is where we call our other functions'''
    n = today()
    print(f'Today is {n}')
    # make use of our imported util
    print( util.checkNumeric(42) )
    print( checkNumeric('42') )


if __name__ == '__main__':
    main() # theere is nothing special about a function called main