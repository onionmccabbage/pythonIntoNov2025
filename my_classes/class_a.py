# there is no relationship between the file name and any class name

class Person: # by convention we use initial cap for class names
    __slots__ = ['__n', '__a'] # the only permitted properties for this class
    # we usually choose to declare an initialization method
    # remember - anything with double underscores fore and aft is part of python
    def __init__(self, n, a): # __init__ will run once every time we create an instance
        self.n = n # self is a way to refer to the created instance
        self.a = a # self.a refers to the get/set methods for 'a'
# Mini-challenge: write get/set decorated methods to validate n as a non empty string
    @property
    def n(self): # remember - methods of a class MUST take 'self' as the first argument
        return self.__n
    @n.setter
    def n(self, new_n):
        if type(new_n)==str and new_n !='':
            self.__n = new_n
        else:
            raise TypeError('Name must be a non-empty string')


    # we often write methods of the class, including property validation methods
    @property # here we decorate our function as a property
    def a(self): # getter or accessor method. This function behaves as a property
        '''this is the property getter method for the value 'a' '''
        # name mangling prevents access t oa mangled propertyn from outside the class
        return self.__a
    # Python never allows funtions to share the same name, except with get/set decorators
    @a.setter # this setter will be invoked whenever we try to mutate the value of 'a'
    def a(self, new_a): # setter or mutator method
        '''this is the property setter method for the value 'a' '''
        if type(new_a)==int and new_a>0:
            self.__a = new_a # __a is called 'name mangling'
        else: # we must decide what will we do if the validation fails
            raise TypeError('Age must be a positive integer') # we might do nothing, or set a sensible default


if __name__ == '__main__':
    '''exercise our code'''
    c = Person('Olga', 32) # we now have an instance of our class (the __init__ runs once)
    f = Person('Floella', 72) # we now have an instance of our class (the __init__ runs once)
    # by default class properties are mutable
    try:
        c.n = ''
        c.a = -42 # [42, 0, True, None]
    except TypeError as te:
        print(te)
    except Exception as err:
        print(f'Something went wring: {err}')
        
    # we may see the values in our class instances
    print(f'Name: {c.n} Age: {c.a}')
    # can we access the name-mangled properties directly?
    print(c.__n) # fail