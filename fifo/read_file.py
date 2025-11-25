# We may retrieve text from a file using file access objects

def readTextFile():
    '''retrieve text from a file using a file access object'''
    try:
        # every file access object is a mechanism to ask the operating system to handle a file
        # we create an _io_wrapper
        # fin = open('my_log.txt', 'r') # r will read (text is the default)
        # print(type(fin))
        # we may use the following simple syntax
        # t = fin.read() # read all the contents of the file
        # fin.close() # it is always a good idea to tidy up and release resources at the earliest opporunity
        # alternatively we may use 'with'
        with open('my_log.txt', 'r') as fin:
            t = fin.read() # retrieves everything as a single string
            # t = fin.readlines() # retrieves a list contaiing each line as a string
            # t = fin.readline() # retrieves the next line
            # t = fin.readline() # the 'with' operator will close() the asset when done
        return t

    # the file may not exist
    except FileNotFoundError as err:
        print(f'No such file {err}')
    except Exception as err:
        print(f'General Error: {err}')

if __name__ == '__main__':
    t = readTextFile()
    print(t, type(t))