# The simplest way to commit text to a file is using print

def printOutput(s):
    '''Persist the incoming string 's' into a text file'''
    # we would probably need to validate that s is a string!!
    # we need a file access object
    fout = open('my_log.txt', 'at') # 'at' will append text (t is the default)
    # NB append will create the file if it doesnt yet exist
    print(s, file=fout) # NB print will always add a new line

if __name__ == '__main__':
    str = 'Here is some text'
    printOutput(str)