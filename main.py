"""Module for the game"""
import street
import character
import item


def main(current_street):
    backpack = []
    health = 30
    dead = False
    while dead == False:
        print("\n")
        print(current_street)

        passerby = current_street.get_character()

        if passerby is not None:
            print(passerby)

        thing = current_street.get_item()
        if thing is not None:
            print(thing)

        print(
            """
Possible actions:
forward         Go to the next street
back            Return to the previous street
talk            Talk to the character on the street
give            Give something to a good person if he is on the street
fight           Fight the enemy if he is on the street
use             Use a first aid kit if it is in a backpack
take            Put the thing from the street to the backpack
backpack        See what's in the backpack
health          See how much health is left
end             Finish the game
        """
        )

        action = input(">>> ")
        if action in ["forward", "back"]:
            current_street = current_street.move(action)
        elif action == "talk":
            if passerby is not None:
                passerby.talk()
            else:
                print("There is nobody to talk with")
        elif action == "fight":
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if isinstance(passerby, character.Boss):
                    if passerby.fight(fight_with):
                        if passerby.is_defeated():
                            print("Congratulations, you won the game!!!")
                            dead = True
                        else:
                            print("You won this fight, keep fighting")

                    else:
                        print("Oh dear, you lost the fight.")
                        health -= 10
                        if health == 0:
                            print("That's the end of the game")
                            dead = True
                        else:
                            print(f"Be careful, you health is {health} now")
                elif isinstance(passerby, character.Enemy):
                    if passerby.fight(fight_with):
                        print("You won this fight")
                        if passerby.item is not None:
                            backpack.append(passerby.item.name)
                            print(f"You got {passerby.item.name}")
                        current_street.add_character(None)

                    else:
                        print("Oh dear, you lost the fight.")
                        health -= 10
                        if health == 0:
                            print("That's the end of the game")
                            dead = True
                        else:
                            print(f"Be careful, you health is {health} now")
                else:
                    print("You can't fight here")
            else:
                print("You don't have a " + fight_with)
        elif action == "give":
            print("What will you give passerby?")
            gift = input()
            if gift in backpack:
                if isinstance(passerby, character.Friend):
                    if passerby.give_item(gift):
                        print(f"You got {passerby.item.name}")
                        backpack.append(passerby.item.name)
                        backpack.remove(gift)
                    else:
                        print(f"{passerby.name} doesn't need {gift}")
                else:
                    print("You can't give someone something here")

        elif action == "use":
            if "first aid kit" in backpack:
                health += 30
                print(f"Your health is {health}")
                backpack.remove("first aid kit")
            else:
                print("You do not have a first aid kit")
        elif action == "take":
            if thing is not None:
                print("You put the " + thing.get_name() + " in your backpack")
                backpack.append(thing.get_name())
                current_street.add_item(None)
            else:
                print("There's nothing here to take!")
        elif action == "backpack":
            if backpack:
                for i in backpack:
                    print(i)
            else:
                print("Ypur backpack is empty:(")
        elif action == "health":
            print(f"Your health is {health}")
        elif action == "end":
            print("Thanks for playing!")
            dead = True
        else:
            print("I don't know how to " + action)


if __name__ == "__main__":
    print(
        """
Welcome to this game!!!
Today you can travel through the 5 streets of Lviv.
Little spoiler: in the end you will meet the boss, and if you beat him, you will win the game.
You will also meet different characters on the streets of Lviv.Some of them can be your friends,
and others are enemies. You can talk with them. Their names are transliterated from Ukrainian.
Friends have some items, and you can get them if you give something in return.
You need to defeat the enemy to also get some things you need.
You can also find something on the streets.
Your health is 30. I hope it’s enough. You also have a backpack where you can find items, which
you collect.
I think you will understand further during the game.
Be careful and good luck !!!

    """
    )
    stryi = street.Street("Stryiska Street")
    stryi.set_description(
        """
Among Lviv's streets, Stryiska is one of the longest (about 7.5 km) streets and one of the 
most populous.Roman Osipovych Shukhevych lived here - a Ukrainian politician and statesman,
commander in chief of the Ukrainian Insurgent Army.
    """
    )
    batiar = character.Enemy(
        "Batiar",
        "Drunkard, popular with women brutal man of the late 19th and early 20th century. ",
    )
    coffee = item.Item("coffee", "lavender latte from the cafeteria of UCU")
    snowballs = item.Weapon("snowballs", "oh, it's so cold")
    batiar.set_weakness("baseball bat")
    batiar.set_converstaion("Hey! Who are you? Do you have whiskey, or beer at least?")
    batiar.set_item(snowballs)
    stryi.add_character(batiar)
    stryi.add_item(coffee)

    koseln = street.Street("Koselnytska Street")
    koseln.set_description(
        """
Here are the buildings of the Ukrainian Catholic University, the Sheptytsky Center, and Trapezna.
    """
    )
    laidak = character.Friend("Laidak", "Poor homeless man")
    laidak.set_converstaion("Oh my God. I feel so sleepy, but I don't have money.")
    baseball_bat = item.Weapon(
        "baseball bat", "it's so heavy, I hope some cool baseball player had it"
    )
    laidak.set_item(baseball_bat)
    laidak.set_needs_of_character("coffee")
    koseln.add_character(laidak)

    franko = street.Street("Ivan Franko Street")
    franko.set_description(
        """
One of the first streets in Lviv in terms of the number of architectural
monuments. There are 52 townhouses on the street, which are monuments of
architecture of local significance and urban planning of Lviv.
    """
    )
    zbrui = character.Enemy("Zbrui", "Robber, burglar.")
    zbrui.set_converstaion("Oh, you have such pretty earings. Are they gold?")
    zbrui.set_weakness("snowballs")
    water_pistol = item.Weapon("water pistol", "it will be useful in hot weather")
    zbrui.set_item(water_pistol)
    lviv_croissant = item.Item("Lviv croissant", "the most delicious dish")
    franko.add_character(zbrui)
    franko.add_item(lviv_croissant)

    shevchenko = street.Street("Taras Shevchenko Street")
    shevchenko.set_description(
        """
One of the seven important transport arteries of Lviv.
    """
    )
    kavaler = character.Friend(
        "Kavaler",
        "A man who entertains a woman in the company, accompanies her on a walk, and so on.",
    )
    kavaler.set_converstaion("Hey, do you like French food?")
    kavaler.set_needs_of_character("Lviv croissant")
    first_aid_kit = item.Support("first aid kit", "it can increase your health")
    kavaler.set_item(first_aid_kit)
    shevchenko.add_character(kavaler)

    krakiv = street.Street("Krakivska Street")
    krakiv.set_description(
        """
Krakivska Street is a street in the historical center of Lviv, one of the oldest streets in the
city. The street got its name from one of the gates to the city.
    """
    )
    lotr = character.Boss("Lotr", "Rogue, robber, robber.")
    lotr.set_converstaion("Do you really think you can beat me?")
    lotr.set_weakness("water pistol")
    krakiv.add_character(lotr)

    stryi.link_street(koseln, "forward")
    koseln.link_street(stryi, "back")
    koseln.link_street(franko, "forward")
    franko.link_street(koseln, "back")
    franko.link_street(shevchenko, "forward")
    shevchenko.link_street(franko, "back")
    shevchenko.link_street(krakiv, "forward")
    krakiv.link_street(shevchenko, "back")

    main(stryi)
