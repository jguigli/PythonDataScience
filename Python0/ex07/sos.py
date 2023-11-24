import sys

DICT_MORSE  = {" " : "/ ",
				"A" : ".- ",
				"B" : "-... ",
				"C" : "-.-. ",
				"D" : "-.. ",
				"E" : ". ",
				"F" : "..-. ",
				"G" : "--. ",
				"H" : ".... ",
				"I" : ".. ",
				"J" : ".--- ",
				"K" : "-.- ",
				"L" : ".-.. ",
				"M" : "-- ",
				"N" : "-. ",
				"O" : "--- ",
				"P" : ".--. ",
				"Q" : "--.- ",
				"R" : ".-. ",
				"S" : "... ",
				"T" : "- ",
				"U" : "..- ",
				"V" : "...- ",
				"W" : ".-- ",
				"X" : "-..- ",
				"Y" : "-.-- ",
				"0" : "----- ",
				"1" : ".---- ",
				"2" : "..--- ",
				"3" : "...-- ",
				"4" : "....- ",
				"5" : "..... ",
				"6" : "-.... ",
				"7" : "--... ",
				"8" : "---.. ",
				"9" : "----. ",
}


def main():
	"""Prend une string en argument et l'imprime en morse"""
	assert len(sys.argv) == 2, "the arguments are bad"
	str = sys.argv[1]

	assert all(char.isalnum() or char.isspace() for char in str), "the arguments are bad"

	result = ""
	for char in str:
		if char.isalpha():
			result += DICT_MORSE[char.upper()]
		else:
			result += DICT_MORSE[char]
	result = result[:-1]
	print(result)


if __name__ == "__main__":
    main()