# we may choose to write our code across several modules
import datetime # we have access to everything in the datetime library

# there is never a problem to including functions within a main module
def today():
    '''provide a nicely formtted date-time string'''
    # if we imported the entire library we must fully qualify our feature calls
    now = datetime.datetime.date( datetime.datetime.today() )
    return now

def main():
    '''By convention this is where we call our other finctions'''
    n = today()
    print(f'Today is {n}')


if __name__ == '__main__':
    main() # theere is nothing special about a function called main