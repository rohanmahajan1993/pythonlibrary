'''
Classes functionality. No real protection from private variables.
'''

class ExampleObject:
   value = 0 # Classvariable 

   @staticmethod #adding this decorator allows you to call it from instance of class
   def class_method():
     print "whats up"
   def __init__(self, n):
	self.n = n
	self.__n = n #python does name mangling but still not technically private
   def sample_method(self):
	print self.n
e = ExampleObject(15)

#instance variables
print e.n
#can't do this because of name mangling print e.__n

#static methods
print ExampleObject.value #can access through static class
print e.value #can access static variables through instance

#instance methods
e.sample_method() 

#class methods
ExampleObject.class_method()

class ExtendedExampleObject(ExampleObject):
  def __init__(self, n):
     ExampleObject.__init__(self,n)
		
exampleObject = ExtendedExampleObject(5)
print exampleObject.n
