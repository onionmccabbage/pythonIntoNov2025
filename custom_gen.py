from datetime import datetime
# Range and generators are great, but we can build our own too

# simple range
r = range(0,10)

# a simple generator expression
temperature = (f'{i}C' for i in range(-70, 91))
for _ in temperature:
    print(_, end='\t')

# we may need to create a dat-time stamp, maybe to use when writing a log file
def makeDT():
    '''Generate a date-time stamp as a nicely formatted string'''
    # we may need our generator to run endlessly
    while True:
    # for i in range(0,10): # this generator will yield ten values then cease
        now = datetime.now()
        dt_str = now.strftime('%d-%m-%y %H:%M:%S') # strftime lets us specify a 'picture' for our date
        # to make an ordinary function behave like a generator, we use 'yield' instead of 'return'
        yield dt_str

if __name__ == '__main__':
    # we need an instance of our generator
    dt = makeDT()
    print(type(dt))
