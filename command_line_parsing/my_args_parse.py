"""
Very basic arg parser that supports types, help, default values, and optional arguments.

"""
import sys
module_name = sys.modules[__name__]

class Argument():
  def __init__(self, name, type, isOptional, help, target):
     self.name = name 
     self.type = type
     self.isOptional = isOptional   
     self.help = help
     self.target = target
  
  def process_argument(self, value_string):     
    print "the value string is", value_string
    converted_value = self.type(value_string)
    setattr(module_name, self.target, converted_value) 

  def __str__(self):
     return self.name   
      
class ArgParser:
  
  def __init__(self):
     self.args_dict = dict()
     self.required_arguments = set() 
  
  def __print_help(self):
     print "whats up"
 
  def add_argument_handler(self, name, type, isOptional, help, target):
       arg = Argument(name, type, isOptional, help, target)
       self.args_dict[name] = arg
       if not isOptional:
	  required_arguments.add(name) 

  def parse_arguments(self):
     copy_required_arguments = self.required_arguments.copy() 
     args = sys.argv[1:]
     for args in args:
	name, value = args.split("=")
	print "name is", name, "value is", value
        arg = self.args_dict[name]
	arg.process_argument(value)
        if not arg.isOptional:
          copy_required_arguments.remove(name)
     for element in copy_required_arguments:
	print "you are missing the following argument", element 
  def print_help(self):
     print "help screen"  	         		

arg_parse = ArgParser()
arg_parse.add_argument_handler("a", int, True, "help message", "a")
arg_parse.parse_arguments()
print a
