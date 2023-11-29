import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """DOC HERE"""
    # manage error
    bmi = [w / (h ** 2) for h, w in zip(height, weight)]
    np.array(heigh)
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """DOC HERE"""
    limit = 