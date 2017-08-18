def list_comprehension():
    x = [1, 2, 3]
    y = [2 * i for i in x]
    print y  

def print_function(s):
   print "the string is ", s
def function_pointer(helper, s):
    helper(s)
def test_function_pointer():
   function_pointer(print_function, "this is working")
test_function_pointer()
    
