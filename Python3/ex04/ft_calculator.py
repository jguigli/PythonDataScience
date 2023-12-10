class calculator:
    """A calculator for performing operations on two list."""

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        result = [e1 * e2 for e1, e2 in zip(V1, V2)]
        print(f"Dot product is : {sum(result)}")

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Add two vectors element-wise."""
        result = [float(e1) + float(e2) for e1, e2 in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Subtract the second vector from the first vector element-wise."""
        result = [float(e1) - float(e2) for e1, e2 in zip(V1, V2)]
        print(f"Sous Vector is : {result}")
