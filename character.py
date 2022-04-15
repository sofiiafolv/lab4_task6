"""Main module for representation of characters"""


class Character:
    """Class for representation of character"""

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.item = None

    def set_converstaion(self, conversation):
        """Adding concersation for talking"""
        self.conversation = conversation

    def __str__(self) -> str:
        if self.item is not None:
            info = self.item.get_name()
        else:
            info = "nothing"

        return f"""
{self.name} is here!
{self.description}
{self.name} has {info}.
"""

    def talk(self) -> None:
        """Prints conversation"""
        print(
            f"""
[{self.name} says]: {self.conversation}
""",
            end="",
        )

    def set_item(self, item):
        """Sets an item instead of None"""
        self.item = item


class Friend(Character):
    """Class for representation of friend"""

    def __init__(self, name, description) -> None:
        super().__init__(name, description)

    def set_needs_of_character(self, needs):
        """An item which friend needs"""
        self.needs = needs

    def give_item(self, item):
        """Returns True if character needs it"""
        if item == self.needs:
            return True
        return False


class Enemy(Character):
    """Class for representation of enemy"""

    def __init__(self, name, description) -> None:
        super().__init__(name, description)

    def set_weakness(self, weakness: str) -> None:
        """Sets the passed argument instead of the self.weakness"""
        self.weakness = weakness

    def fight(self, weapon: str) -> bool:
        """Returns a bool value if is enemy is defeated"""
        if self.weakness == weapon:
            return True
        return False


class Boss(Enemy):
    """Class for representation of boss"""

    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.health = 30

    def fight(self, weapon: str) -> bool:
        """Returns a bool value if is enemy is defeated"""
        if self.weakness == weapon:
            self.health -= 10
            return True
        return False

    def is_defeated(self):
        """Returns a bool value if boss health = 0 and he is defeated"""
        if self.health == 0:
            return True
        return False
