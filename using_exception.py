# We may check and handle exceptions
# especially useful when the outcome is not entirely predictable
# We may have pure functions, where the outcome is absolutely predicatble based on the inputs

# using input is unreliable we cannot predict the user response
def myFn():
    '''ask for user input then work with the result'''
    response = input('Please enter a positive integer 0-100: ')
    # we need to make sure the string is numeric
    try:
        n = int(float(response))
        # if there was no exception our code reaches here
        if n not in range(0, 101):
            raise TypeError('Number must be 0-100')
    except ValueError as err: # we may choose to handle specific kinds of exception
        print(f'There is a problem {err}')
    except TypeError as err:
        print(err)
    except Exception as err:
        print(f'A more serious problem occured {err}')
    finally:
        print('The finally block will always run, whether or not we had an exception')



if __name__ == '__main__':
    '''this is where we exercise the code'''
    myFn()
    myFn() # even if there was an exception we can continue to run our code