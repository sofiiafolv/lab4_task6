"""Main module for representation of streets"""


class Street:
    """Class for representation of streets in the game"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.description = None
        self.directions = [None, None]
        self.character = None
        self.item = None

    def set_description(self, description: str) -> None:
        """Setting a description of street"""
        self.description = description

    def link_street(self, street: object, direction: str) -> None:
        """Linking streets"""
        if direction == "forward":
            self.directions[0] = street
        elif direction == "back":
            self.directions[1] = street

    def add_character(self, character: object) -> None:
        """Sets the passed argument instead of the self.character"""
        self.character = character

    def add_item(self, item: object) -> None:
        """Sets the passed argument instead of the self.item"""
        self.item = item

    def get_character(self) -> object:
        """Returns characters on the street"""
        return self.character

    def get_item(self) -> object:
        """Returns items on the street"""
        return self.item

    def __str__(self) -> str:
        details = self.name + "\n-------------------\n" + self.description + "\n"
        for d in self.directions:
            if d is not None:
                if self.directions.index(d) == 0:
                    location = "forward"
                elif self.directions.index(d) == 1:
                    location = "back"
                details += f"{d.name} is {location}\n"
        return details

    def move(self, direction: str) -> None:
        """Moving on another street"""
        if direction == "forward" and self.directions[0] is not None:
            self = self.directions[0]
        elif direction == "back" and self.directions[1] is not None:
            self = self.directions[1]
        else:
            print(f"You can't move {direction}")
        return self
