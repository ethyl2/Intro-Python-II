# Implement a class to hold room information. This should have name and
# description attributes.

"""Put the Room class in room.py based on what you see in adv.py.

The room should have name and description attributes.

The room should also have n_to, s_to, e_to, and w_to attributes 
which point to the room in that respective direction.
"""


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''

    def __str__(self):
        return f'{self.name}, {self.description}'
