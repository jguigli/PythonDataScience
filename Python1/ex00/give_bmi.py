import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
        ) -> list[int | float]:
    """Calculate BMI with two list (heigh and weight)
     by numpy operation and returns a list"""
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("Elements list must be int or float")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Elements list must be int or float")

    if len(height) != len(weight):
        raise ValueError("Lists must have the same length")

    height_bmi = np.array(height)
    weight_bmi = np.array(weight)

    bmi = weight_bmi / height_bmi ** 2
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list containing true or false depending on the limit"""
    if not all(isinstance(v, (int, float)) for v in bmi):
        raise TypeError("Elements list must be int or float")
    if not isinstance(limit, int):
        raise TypeError("Limit must be int")

    bmi_np = np.array(bmi)
    bmi_bool = bmi_np > limit
    return bmi_bool.tolist()
