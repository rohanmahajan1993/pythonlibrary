import classes
a = classes.ExampleObject(5)

#Tools for instance directory
print "dir calls", dir(a) #dir will look at parent classes and will print both methods and state
print "dict calls", a.__dict__ #just prints out state for the object

#Tools for classes 
print "classes file", classes.__file__ # prints out the classes file
for i in range(10):
   print "   "
print dir(classes.ExampleObject) #both do similar stuff here
print classes.ExampleObject.__dict__

"""Use pdb which is pretty much gdb"""
import pdb
pdb.set_trace()



