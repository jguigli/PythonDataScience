from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character.
    This class is meant to be subclassed to create specific character types."""

    def __init__(self, first_name, is_alive=True):
        """Initialize the object with specific class variables.
        Set is_alive to True if the parameter is not specified."""
        self.first_name = first_name
        self.is_alive = is_alive
        pass

    @abstractmethod
    def die(self):
        """Handle the state is_alive of the object."""
        pass


class Stark(Character):
    """Concrete class representing a Stark character.
    This class inherits from the abstract base class Character and provides
    a specific implementation for the die() method."""

    def die(self):
        """Modify the state of the class variable is_alive to False"""
        self.is_alive = False
