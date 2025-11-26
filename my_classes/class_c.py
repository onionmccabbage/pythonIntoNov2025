from class_a import Person
# We may use any class the basis for a new class. This is alled inheritance
l = list((4,3,2))
print( type(l) ) 

# We may inherit from the built in classes
class MyList(list): # NB many of the build on object (classes) do not use initial caps
    pass

class CustomException(Exception):
    '''this is our own exception type'''

# we may also inherit from our own classes
class User(Person):
    '''All the features of Person are available in this class
    This User clss also includes a list of user permissions'''
    def __init__(self, n, a, new_perm):
        super().__init__(n, a) # call the __init__ of the parent class
        # for collection types we often initialize the empty collection
        self.__perm = [] # we start with n empty list
        self.perm = new_perm
    @property
    def perm(self):
        return self.__perm
    @perm.setter
    def perm(self, new_p):
        '''if new_p is a non-empty string, add it to the permission list
        If it is a list, append all members of it to the existing perm'''
        if type(new_p)==str and new_p !='':
            self.__perm.append(new_p)
        elif type(new_p)==list:
            for _ in new_p:
                self.__perm.append(_)

if __name__ == '__main__':
    # we may crate instances of our own classes
    l1 = MyList()
    l1.append(3)
    l1.append(2)
    l1.append(1)
    l1.append(0)
    print(l1, type(l1))
    # raise CustomException('now thats clever')
    # use our User class
    n = User('Goethe', 23, ['user', 'admin'])
    n.perm = 'superuser'
    n.perm = ['guest', 'expert']

    print(n.perm)
