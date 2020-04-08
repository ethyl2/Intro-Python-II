# Write a class to hold player information, e.g. what room they are in
# currently.
"""Players should have a name and current_room attributes.

----

Add capability to add Items to the player's inventory. 
The inventory can also be a list of items "in" the player, 
similar to how Items can be in a Room.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = ''
        self.items = []

    def __str__(self):
        return f'{self.name} is in the {self.current_room}.\n'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        print(f'Current inventory of {self.name}:')
        index = 1
        for item in self.items:
            print(f'\t{index}. {item.name}')
            index += 1
