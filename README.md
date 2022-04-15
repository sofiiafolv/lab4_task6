# lab4_task6

## Description
There are 4 modules.
street.py for Street class
character.py for classes Character, Friend, Enemy, Boss. Friend and enemy are inherited from Character, and Boss is inherited from Enemy.
item.py for class Item, Support, Weapon. Support and Weapon are inherited from Item, but in fact they are just classes with pass.
main.py the main cycle of the game.

## street.py
Based on the Room class from the previous task.
It has same attributes: name, item, character, description. It also has directions intaed of rooms. It is a list with two elements, which are initially None.

Methods are also the same.

In method set_description(self, description) the description attribute is created.

link_street(self, street, directions)
0 - forward, 1 - back. It works like link_rooms. Depending on location, one of the element in a list is changed to instance of the class Street.

add_character and add_item Just sets passed arguments instead of attributes self.character and self.item, which are previously None.

get_character and get_item return an instance of the class or None if there no character or item.

move(self, direction) According to the indexes and directions mentioned earlier, changes one instance of the class and all its attributes to another, if the list item is not equal to None. If None, print that you cant go there.

__str__(self) Returns a string representation. First, create a string with the attributes self.name and self.description, and then if there are any streets in the list other than None, then add a string about the location of this street.

## character.py
Based on the Character class from the previous task

### Character

Attributes: name, description, conversation, item.

set_conversation(self, conversation) Creates a conversation attribute and references the passed argument.

talk() Just prints conversation

__str__(self) Just prints a string with self.name and self.description and self.item.name if self.item is not None.

set_item(self, item) Some characters can have items which can help beat enemies. So this method just sets an instance of class Item or its subclasses instead of None.

### Friend

set_needs_of_character(self, needs) Every friend has some needs(you have hints about them in conversations). They will give you something in return, if you give then an item which they need. So this method just creates new attribute self.needs and sets a passed argument.

give_item(self, item) If item == self.needs, returns True, and you can get other items, This will be described below. Otherwise returns False.

### Enemy

set_weakness(self, weakness) Creates a weakness attribute and references the passed argument.

fight(self, weapon). Check if passes argument is equal to self.weakness. Returns True if weapon == self.weakness, the player wins the fight, else returns False and player loses, game is ended.

### Boss

Boss has new attribute health which is equal to 30.

fight(sself, weapon) It works like the method from Enemy, but it also reduces health and you need to win three times to defeat the Boss.

is_defeated(self) Checks if health == 0, and returns True, else returns False. If health == 0, game ends, player wins.

## item.py
Based on the Item class from the previous task.
Attributes: name, description

In method set_description(self, description) the description attribute is created.

__str__(self) Returns string with self.name and self.description

get_name() returns a name of item to put in back pack

## main.py
Quite similar to the module from the previous task.

First, prints info about game rules and its process, instanсes of all classes are added, rooms are connected, information about the streets, characters and items is provided. You can meet someone on every street, and some have objects. I don't think it needs to be explained, most of it is like in the previous task module, only more characters, streets and objects.

The main cycle is in function main(current_street). Initially, current street is Stryiska.
The game continues until the variable is False.
Every time info about street, passerbies, items on the street and action which player can do. Game accepts input from the player and performs a specific action.

### forward and back
The method move() described above is called and current_street now references another object.

### talk
If there is a character on this street method talk() is called.

### fight
There are different developments of the game. Game accepts input from the player. If input is in backpack, passerby is Boss, and this input is his weakness, method fight() is called. Also method is_defeated checks if health of Boss == 0. If it is True, you win the game. If input is not his weakness, the player's health is reduced by 10. If the player's health == 0, the game is ended.
If it is just an Enemy, the method fight() is called and if it is a weakness, you win the fight, if Enemy's item is not None, it will be put in your backpack. This enemy is not on the street anymore.
If passerby is not Enemy or Boss, you cant fight with them.
If input is not in your backpack, you will get a string on the screen info that the item you chose is not in your backpack.

### give
Game accepts input from the player. If character is an istance of class Friend, you can give this input to them if it is in your backpack. The method give_item() is called. If True you can get a passerby.item if it is not None. If False you will see the string that passerby doesn't need this item. The item which you gave will be removed from your backpack.

### use
If first_aid_kit in you backpack, health will increase by 30. First aid kit will be removed from your backpack.

### backpack
every item in backpack will be printed

### health 
Your health will be printed

### end
dead == True, the game is ended. If you don't want to play game till the end, you can just write 'end'.

### else
If there is no such action. You will get a string about that on the screen.
