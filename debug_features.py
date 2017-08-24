import classes
import imp
import dis
def tester():
   print "whats up"
dis.dis(tester)
a = classes.ExampleObject(5)

#Tools for instance directory
print "dir calls", dir(a) #dir will look at parent classes and will print both methods and state
print "dict calls", a.__dict__ #just prints out state for the object

#Tools for classes 
print "classes file", classes.__file__ # prints out the classes file
print imp.find_module('classes') #helps you search different classes

print dir(classes.ExampleObject) #both do similar stuff here
print classes.ExampleObject.__dict__

print id(a) #gets you the memory address

print imp.find_module('numpy') # shows you path where module is defined

print globals() #shows  you all the globals that are defined currently
print locals() #shows  you local information

x = 5
print eval('x + 1') # runs this code 

"""Use pdb which is pretty much gdb"""
import pdb
pdb.set_trace()



