def square(x: int | float) -> int | float:
    """Calculate the square of a number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Calculate the power of a number to itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Create a closure that applies a function to an internal variable."""
    count = x

    def inner() -> float:
        """Apply the specified function to the internal variable."""
        nonlocal count
        result = function(count)
        count = result
        return result
    return inner
