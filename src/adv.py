from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
indiana = Player('Indiana Jones')
indiana.current_room = room['outside']


necklace = Item('necklace', 'a sparkly string of interesting gems')
ring = Item('ring', 'engraved in an unknown language')
broom = Item('broom', 'falling apart from much use')
spider = Item('spider', 'a long-legged fuzzy creature')
candle = Item('candle', 'almost burnt down to nothing')

room['outside'].add_item(broom)
room['outside'].add_item(candle)
room['treasure'].add_item(spider)
room['foyer'].add_item(ring)
room['foyer'].add_item(necklace)


'''
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# Valid commands are n, s, e and w which move the player North, South, East or West
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
'''
directions = {
    'n': 'north',
    's': 'south',
    'e': 'east',
    'w': 'west',
    'q': 'home'
}


def move_error(action):
    return f"{indiana.name} can't go {directions[action]}. Make another choice."


def print_items(room):
    index = 1
    if len(room.items) > 0:
        print(f'In {room.name}: ')
    for item in room.items:
        print(f'\t {index}. {item}')
        index += 1
    print('\n')


inPlay = True
while inPlay:
    print(indiana)
    print_items(indiana.current_room)
    action = input(
        f'Choose one: [n] go north, [s] go south, [e] go east, [w] go west, [q] quit.\n')

    if action not in directions.keys():
        print(f'{action} is an invalid choice. Try again.')
    else:
        print(f'\n{indiana.name} wants to go {directions[action]}.')

    if action == 'n':
        if indiana.current_room.n_to != '':
            indiana.current_room = indiana.current_room.n_to
        else:
            print(move_error(action))

    elif action == 's':
        if indiana.current_room.s_to != '':
            indiana.current_room = indiana.current_room.s_to
        else:
            print(move_error(action))

    elif action == 'e':
        if indiana.current_room.e_to != '':
            indiana.current_room = indiana.current_room.e_to
        else:
            print(move_error(action))

    elif action == 'w':
        if indiana.current_room.w_to != '':
            indiana.current_room = indiana.current_room.w_to
        else:
            print(move_error(action))

    elif action == 'q':
        inPlay = False
