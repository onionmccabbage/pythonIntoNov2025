# why would we bother using classes?

# we use data types to capture data
age = 42        # integer
fn = 'Floella'  # string
obe = True      # boolean

f = (42, 'Floella', True)

fd = {'age':42, 'fb':'Floella', 'o':True, 'langs':('Python', 'C')}

# all these built in structures are immensely useful
# but they lack a few features
# no built in validation of data content or type
# no guard against arbitrary additional members
# no way to check we have all the data members we need

# All the above features can be attained by using a class
# We may also attach functions to our class - methods


