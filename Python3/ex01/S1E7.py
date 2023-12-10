from S1E9 import Character


class Baratheon(Character):
    """Concrete class representing a Baratheon character.
    This class inherits from the abstract base class Character and provides
    a specific implementation for the die() method."""
    def __init__(self, first_name, is_alive=True):
        """Initialize class variables first_name and is_alive.
        Set is_alive to True if the parameter is not specified"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Modify the state of the class variable is_alive to False"""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character."""
        s = f"Vector : ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return s

    def __repr__(self):
        """Return a string representation of the
         character for debugging purposes."""
        return self.__str__()


class Lannister(Character):
    """Concrete class representing a Lannister character.
    This class inherits from the abstract base class Character and provides
    a specific implementation for the die() method."""
    def __init__(self, first_name, is_alive=True):
        """Initialize class variables first_name and is_alive.
        Set is_alive to True if the parameter is not specified"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Modify the state of the class variable is_alive to False"""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character."""
        s = f"Vector : ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return s

    def __repr__(self):
        """Return a string representation of
         the character for debugging purposes."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """Create a Lannister character with the specified attributes."""
        return cls(first_name, is_alive)
