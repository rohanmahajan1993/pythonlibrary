'''
With statements are basically like try and finally.
Any class can be implemented as long they have init funciton
'''
class WithClass():
    def __init__(self, x):
	print "calling the init class"
        self.x = x
    def __enter__(self):
        print "calling the enter function"
        return self
    def __exit__(self, type, value, traceback):
	print "calling the exit function"
    def test_function(self):
	print "testing function"
with WithClass(3) as f:
     f.test_function()
