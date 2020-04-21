"""Item class

The item should have name and description attributes.

Hint: the name should be one word for ease in parsing later.
This will be the base class for specialized item types to be declared later.

-----

Add an on_take method to Item.

Call this method when the Item is picked up by the player.

on_take should print out "You have picked up [NAME]" when you pick up an item.

The Item can use this to run additional code when it is picked up.

----

Add an on_drop method to Item. Implement it similar to on_take.

---
Add a subclass to Item called LightSource.

"""


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'

    def on_take(self, player_name='You', verb_form='have'):
        print(
            f'\033[0;33;44m {player_name} {verb_form} picked up the {self.name}.')

    def on_drop(self, player_name='You', verb_form='have'):
        print(
            f'\033[1;37;41m {player_name} {verb_form} dropped the {self.name}.')


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self, player_name='You', verb_form='have'):
        """
        Override on_drop in LightSource that tells the player 
        "It's not wise to drop your source of light!" if the player drops it. 
        (But still lets them drop it.)
        """
        print("\033[1;31;40m It's not wise to drop your source of light!")
        super(LightSource, self).on_drop()
