PYTHON_PREFIX = "::"
PYTHON_PREFIX_LEN = len(PYTHON_PREFIX)

def read_file(filename):
   with open(filename, "rb") as fp:
    bytes = fp.readlines()
    return bytes

def analyze_template_synthax(line, indentation_count):
    print "entering template synthax"
    #-1 is good get rid of new_linecharacter
    new_line = "print \"" + line[:-1] +"\"" + "\n" 
    indented_new_line = ' ' * indentation_count + new_line
    return indented_new_line

def analyze_python_synthax(line, indentation_count):
    print "entering answering python synthax", line
    new_line = line[PYTHON_PREFIX_LEN:]
    stripped_new_line = new_line.lstrip()
    if stripped_new_line == "endfor\n" or stripped_new_line == "endif\n":
       new_line = "\n"
    elif stripped_new_line.startswith("for") or stripped_new_line.startswith("if"):
       indentation_count += 2 
    return new_line, indentation_count

def transform_template_lines(script_lines):
   indentation_count = 0
   for i in range(len(script_lines)):
       line = script_lines[i]
       if line.startswith(PYTHON_PREFIX):
         new_line, indentation_count = analyze_python_synthax(line, indentation_count)
       else:
	 new_line = analyze_template_synthax(line, indentation_count)
       script_lines[i] = new_line	
   return script_lines

def run(filename, variables):
   template_lines = read_file(filename)
   script_lines = transform_template_lines(template_lines)
   script = "".join(script_lines)
   print "the script is", script
   exec(script, variables)
