# Implement a class to hold room information. This should have name and
# description attributes.

"""Put the Room class in room.py based on what you see in adv.py.

The room should have name and description attributes.

The room should also have n_to, s_to, e_to, and w_to attributes 
which point to the room in that respective direction.

---
Add the ability to add items to rooms.

The Room class should be extended with a list that holds the Items 
that are currently in that room.

Add functionality to the main loop that prints out all the 
items that are visible to the player when they are in that room.

---

Add an attribute to Room called is_light that is True if the Room 
is naturally illuminated, or False if a LightSource is required to 
see what is in the room.
"""


class Room:
    def __init__(self, name, description, is_light=False):
        self.name = name
        self.description = description
        self.n_to = ''
        self.s_to = ''
        self.e_to = ''
        self.w_to = ''
        self.items = []
        self.is_light = is_light
        self.question = ''
        self.answer = ''

    def __str__(self):
        if len(self.items) > 0:
            return f'{self.name}, which contains {len(self.items)} items. {self.description}'
        else:
            return f'{self.name}. {self.description}'

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def print_items(self):
        index = 1
        if len(self.items) > 0:
            print(f'\033[0;34;40m Items in {self.name}: ')
        for item in self.items:
            print(f'\t {index}. {item}')
            index += 1
        print('\n')

    def add_question(self, question):
        self.question = question

    def add_answer(self, answer):
        self.answer = answer

    def print_question(self):
        print(f"\033[1;37;40m A deep voices asks, '{self.question}' \033[m")
