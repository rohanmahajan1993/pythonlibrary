import argparse
#Amazing tutoiral on argparse https://docs.python.org/2/howto/argparse.html

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
parser.add_argument("square", help="display a square of a given number")
print args.echo
