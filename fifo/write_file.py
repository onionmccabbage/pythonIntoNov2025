# Sometimes we need more control when persisting in a text file

def writeTextFile(s):
    '''Commit the string 's' to a text file using write()'''
    try:
        with open('my_log.txt', 'at') as fout: # we could use 'xt' for exclusive file access
            # Careful: by default write() does not add a new line character
            fout.write(f'{s}\n') # write() sill ommit the entire string uing the file access object
            # no need to close()
    except FileNotFoundError as err:
        print(f'No such file {err}')
    except Exception as err:
        print(f'General Error: {err}')


if __name__ == '__main__':
    s = 'writing to a file'
    writeTextFile(s)
