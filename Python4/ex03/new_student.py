import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random ID consisting of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a class student with a name,
     surname, and optional active status."""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Initializes the login attribute based on the name and surname."""
        self.login = f"{self.name[0]}{self.surname}"
