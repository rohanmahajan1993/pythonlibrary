'''
Iterators can be passed in to many built in functions and also are used in for loops.
All that is required is that we have a iter method that returns an object that can has next init.
Usually, one class does both. 
'''

class IterableObject:
   def __init__(self, n):
   	self.i = 0
	self.n = n
   def __iter__(self):
	return self
   def next(self):
	if self.i < self.n:
	  self.i +=1
 	  return self.i
	else:
	  raise StopIteration()
iterable = IterableObject(10)
for i in iterable:
   print i

"""
The generator synthax provides a more convenient way to implement generators.
"""

def first(n):
   num = 0
   while num < n:
	yield num
	num +=1
a = first(10)
for i in a:
   print i 
