class calculator:
    """A simple calculator for performing operations on a list."""

    def __init__(self, list):
        """Initialize the class variable list"""
        self.list = list

    def __add__(self, scalar) -> None:
        """Add a scalar value from each element of the list."""
        self.list = [element + scalar for element in self.list]
        print(self.list)

    def __mul__(self, scalar) -> None:
        """Multiply each element of the list by a scalar value."""
        self.list = [element * scalar for element in self.list]
        print(self.list)

    def __sub__(self, scalar) -> None:
        """Subtract a scalar value from each element of the list."""
        self.list = [element - scalar for element in self.list]
        print(self.list)

    def __truediv__(self, scalar) -> None:
        """Divide each element of the list by a non-zero scalar value."""
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        self.list = [element / scalar for element in self.list]
        print(self.list)
