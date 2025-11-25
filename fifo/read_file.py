# We may retrieve text from a file using file access objects

def readTextFile():
    '''retrieve text from a file using a file access object'''
    try:
        fin = open('my_log.txt', 'r') # r will read (text is the default)
        t = fin.read() # read all the contents of the file
        fin.close() # it is always a good idea to tidy up and release resources at the earliest opporunity
        return t

    # the file may not exist
    except FileNotFoundError as err:
        print(f'No such file {err}')
    except Exception as err:
        print(f'General Error: {err}')

if __name__ == '__main__':
    t = readTextFile()
    print(t)