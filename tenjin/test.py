import tenjin

def test1():
   variables = dict()
   variables["a"] = 6
   variables["b"] = 7
   tenjin.run("script.py", variables)
test1()
