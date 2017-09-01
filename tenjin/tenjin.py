TEMPLATE_PREFIX = "::"
TEMPLATE_PREFIX_LEN = len(TEMPLATE_PREFIX)

def read_file(filename):
   with open(filename, "rb") as fp:
    bytes = fp.readlines()
    return bytes


def analyze_template_synthax(line, stack):
    print "entering template synthax"
    new_line = "print \"" + line[TEMPLATE_PREFIX_LEN:-1] +"\"" + line[-1]    
    return new_line
def analyze_python_synthax(line, stack):
    print "entering answering python synthax"
    newline = line
    return newline
def transform_template_lines(script_lines):
   stack = []
   for i in range(len(script_lines)):
       line = script_lines[i]
       if line.startswith(TEMPLATE_PREFIX):
         new_line = analyze_template_synthax(line, stack)
       else:
	 new_line = analyze_python_synthax(line, stack)
       script_lines[i] = new_line	
   return script_lines

def run(filename, variables):
   template_lines = read_file(filename)
   script_lines = transform_template_lines(template_lines)
   script = "".join(script_lines)
   print script_lines
   exec(script, variables)
