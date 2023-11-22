import sys

assert len(sys.argv) >= 2, "more than one argument is provided"

check = sys.argv[1]

assert check.isdigit(), "argument is not an integer."

nombre = int(check)
if nombre % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")