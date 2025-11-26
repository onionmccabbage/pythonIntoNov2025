# there is no relationship between the file name and any class name

class Person: # by convention we use initial cap for class names
    # we usually choose to declare an initialization method
    # remember - anything with double underscores fore and aft is part of python
    def __init__(self, n, a): # __init__ will run once every time we create an instance
        self.n = n # self is a way to refer to the created instance
        self.a = a


if __name__ == '__main__':
    '''exercise our code'''
    c = Person('Olga', 32) # we now have an instance of our class (the __init__ runs once)
    f = Person('Floella', 72) # we now have an instance of our class (the __init__ runs once)