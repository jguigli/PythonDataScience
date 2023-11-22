import sys

assert len(sys.argv) <= 2, "more than one argument is provided"

if len(sys.argv) == 1:
	sys.exit()

check = sys.argv[1]

assert check.lstrip('-').isdigit(), "argument is not an integer."

nombre = int(check)
if nombre % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")