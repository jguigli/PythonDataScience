from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Concrete class representing a King character.
    This class inherits from the class Baratheon and Lannister.
    This class implements the methods set_eyes, set_hairs,
    get_hairs, and get_eyes."""

    def set_eyes(self, color):
        """Set the eyes color to the specified color."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hair color to the specified color."""
        self.hairs = color

    def get_eyes(self):
        """Return the eye colors"""
        return self.eyes

    def get_hairs(self):
        """Return the hair colors"""
        return self.hairs
