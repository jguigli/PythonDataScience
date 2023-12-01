import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """DOC HERE"""
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not isinstance(start, int) and not isinstance(end, int):
        raise TypeError("Start and end must be int")

    balise = len(family[0])

    for sub in family:
        if (balise != len(sub)):
            raise TypeError("Sublists don't have the same size")


    arr = np.array(family)
    print("My shape is :", arr.shape)
    row, col = arr.shape
    new_arr = arr[start:end, 0:col]
    print("My new shape is :", new_arr.shape)
    return new_arr.tolist()