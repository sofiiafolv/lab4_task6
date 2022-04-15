"""Main module for representation of items"""


class Item:
    """Class for represenation of item"""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __str__(self) -> str:
        """Prints info about item"""
        return f"""
The [{self.name}] is here - {self.description}
"""

    def get_name(self) -> str:
        """Returns name of item"""
        return self.name


class Weapon(Item):
    """Class for representation of weapon"""

    pass


class Support(Item):
    """Class for representation of support"""

    pass
