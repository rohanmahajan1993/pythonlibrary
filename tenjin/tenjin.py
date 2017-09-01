def read_file(filename):
   with open(filename, "rb") as fp:
    bytes = fp.read()
    return bytes

def run_object():
   print 5 

def run(filename, variables):
   script = read_file(filename)
   exec(script, variables)
