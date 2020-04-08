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

"""


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'

    def on_take(self, player_name='You', verb_form='have'):
        print(f'{player_name} {verb_form} picked up the {self.name}.')

    def on_drop(self, player_name='You', verb_form='have'):
        print(f'{player_name} {verb_form} dropped the {self.name}.')
