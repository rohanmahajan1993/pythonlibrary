import sys
import my_args_parse
import cStringIO

def setup():
  stdout_ = sys.stdout #Keep track of the previous value.
  stream = cStringIO.StringIO()
  sys.stdout = stream
  return stream, stdout_

def test1():
  arg_parse = my_args_parse.ArgParser()
  arg_parse.add_argument_handler("a", int, True, "a is some useless parameter", "a")
  arg_parse.add_argument_handler("b", int, True, "b is some useless parameter", "b")
  test_args = ["a=5", "b=6"]
  arg_parse.parse_arguments(test_args)
  assert(5 == my_args_parse.a)
  assert(6 == my_args_parse.b)

def test_help():
  arg_parse = my_args_parse.ArgParser()
  arg_parse.add_argument_handler("a", int, True, "a is some useless parameter", "a")
  test_args = ["--help"]
  stream, old_stdout = setup()
  arg_parse.parse_arguments(test_args)
  variable = stream.getvalue()  
  sys.stdout = old_stdout 
  assert(variable == "a is some useless parameter\n")
  assert(5 == my_args_parse.a)

def test_help():
  arg_parse = my_args_parse.ArgParser()
  arg_parse.add_argument_handler("a", int, True, "a is some useless parameter", "a")
  test_args = ["--help"]
  stream, old_stdout = setup()
  arg_parse.parse_arguments(test_args)
  variable = stream.getvalue()  
  sys.stdout = old_stdout 
  assert(variable == "a is some useless parameter\n")
  assert(5 == my_args_parse.a)

def test_optional():
  arg_parse = my_args_parse.ArgParser()
  arg_parse.add_argument_handler("a", int, True, "a is some useless parameter", "a")
  arg_parse.add_argument_handler("b", int, False, "a is some useless parameter", "a")
  test_args = ["a=7"]
  stream, old_stdout = setup()
  arg_parse.parse_arguments(test_args)
  variable = stream.getvalue()  
  sys.stdout = old_stdout 
  assert(variable == "you are missing the following argument b\n")

test1()
test_help()
test_optional()
