'''
Decorators basically help wrap methods with a method called before and a method call after.
It doesn't have the guarenteed exit functionality that the with functions have.
'''

def wrapper(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
	print "before wrapper"
        some_function()
	print "after wrapper"
    return wrapper

@wrapper
def some_function():
    print "calling the function"

some_function()
