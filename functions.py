def function_pointer():
  print "whats up"

def tester_function(fn):
   fn()

tester_function(function_pointer)
