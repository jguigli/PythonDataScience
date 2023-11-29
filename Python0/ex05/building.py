import sys
import string


def analyse_str(str):
    """Cette fonction recoit une string en argument et retourne
     le nombre de caracteres total ainsi que le nombre de caracteres
      upper, lower, space, digit et punctuation"""
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    digit = 0

    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1

    print("The text contains", len(str), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuations marks")
    print(space, "spaces")
    print(digit, "digits")


def main():
    """Ce programme permet de recevoir un argument en tant que
     string afin de donner des informations sur celle-ci.
      Si aucun argument est donne, le programme lit sur stdin"""
    sys.tracebacklimit = 0

    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) != 2 or sys.argv[1] is None:
        print("What is the text to count ?")
        input = sys.stdin.read()
        analyse_str(input)
    else:
        analyse_str(sys.argv[1])


if __name__ == "__main__":
    main()
