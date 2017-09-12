import tenjin

def test1():
   variables = dict()
   variables["a"] = 6
   variables["bbc"] = 7
   tenjin.run("script.pyx", variables)
test1()
