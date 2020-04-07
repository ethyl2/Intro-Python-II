# Write a class to hold player information, e.g. what room they are in
# currently.
"""Players should have a name and current_room attributes
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = ''

    def __str__(self):
        return f'{self.name} is in the {self.current_room}.\n'
