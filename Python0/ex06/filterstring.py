import sys
import string


def main():
    """Prend une string et un entier en argument et
     imprime une liste contenant chaque mot de la string superieur a N"""

    sys.tracebacklimit = 0

    assert len(sys.argv) == 3, "the arguments are bad"

    S = sys.argv[1]
    N = sys.argv[2]

    assert isinstance(S, str) and N.isdigit(), "the arguments are bad"
    for char in S:
        assert (
            char not in string.punctuation and char.isprintable()
        ), "the arguments are bad"

    newlist = [word for word in S.split() if (lambda x: len(x) > int(N))(word)]
    print(newlist)


if __name__ == "__main__":
    main()
