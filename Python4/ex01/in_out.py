def square(x: int | float) -> int | float:
    """DOC"""
    return x ** 2

def pow(x: int | float) -> int | float:
    """DOC"""
    return x ** x


def outer(x: int | float, function) -> object:
    """DOC"""
    count = x
    def inner() -> float:
        """DOC"""
        nonlocal count
        result = function(count)
        count = result
        return result
    
    return inner