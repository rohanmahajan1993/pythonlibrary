def function_pointer():
  print "whats up"

def tester_function(fn):
   fn()

#* mean list of non_named arguments
def args_function(*arg_list):
   for arg in arg_list:
	print arg

## ** meands dict of named functions
def kargs_function(**args_dict):
   for key, value in args_dict.iteritems():
	print key, value

def parameter_function(a=5, b=6, c=6):
   print a, b, c

tester_function(function_pointer)
sample_list = [1, 2, 3]
print args_function(*sample_list)
sample_dict = {"1":2, "3":4, "5":6}
print kargs_function(**sample_dict)
parameter_function()
parameter_function(5, 6)
parameter_function(c=7)
parameter_function(b=3, c=7)
