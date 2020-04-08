from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east, and west."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'lake_room': Room("Underground Lake Chamber", """In the middle of the large chamber is
a deep, dark lake. If you hug the edges of the room as you walk, you should be able to make it 
across the chamber. If not, it's time to swim! The chamber has a exit to the west and north."""),

    'bone_pit': Room("Pit of Bones", """This depressing room is littered with scattered bones.
Looks like a dead end, in more ways than one."""),

    'cathedral': Room("Grand Cathedral", """The ceiling soars high above you. Inside this cavern 
are some of the most beautiful formations you've ever seen, including a large stalagmite forest 
and a 'frozen' waterfall. You gaze in awe for a while; unfortunately, it looks like the only way 
out is the way you came in.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['lake_room']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['lake_room'].e_to = room['foyer']
room['lake_room'].w_to = room['bone_pit']
room['lake_room'].n_to = room['cathedral']
room['bone_pit'].e_to = room['lake_room']
room['cathedral'].s_to = room['lake_room']

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
    'q': 'home',
    'i': 'look in the inventory',
    'inventory': 'look in the inventory'
}


def move_error(action):
    return f"{indiana.name} can't go {directions[action]}. Make another choice."


'''
Implement support for the verb get followed by an Item name. This will be used to pick up Items.

If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.

If it is there, remove it from the Room contents, and add it to the Player contents.

If it's not there, print an error message telling the user so.

---------

Implement support for the verb drop followed by an Item name. This is the opposite of get/take.
'''


def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False


inPlay = True
while inPlay:
    print(indiana)
    indiana.current_room.print_items()
    action = input(
        f"Choose one: go [n] north, [s] south, [e] east, [w] west, [i] show inventory, [q] quit OR type 'get [item]' OR 'drop [item]'.\n")

    action_split = action.split(' ')
    if len(action_split) == 2:
        if action_split[0] == 'get' or action_split[0] == 'take':
            matches = [
                x for x in indiana.current_room.items if x.name == action_split[1]]

            if len(matches) > 0:
                indiana.current_room.remove_item(matches[0])
                indiana.add_item(matches[0])
                matches[0].on_take(indiana.name, 'has')
            else:
                print(
                    f'{action_split[1]} is not found in the {indiana.current_room.name}. Try again.')
        elif action_split[0] == 'drop':
            matches = [
                x for x in indiana.items if x.name == action_split[1]]
            if len(matches) > 0:
                indiana.current_room.add_item(matches[0])
                indiana.remove_item(matches[0])
                matches[0].on_drop(indiana.name, 'has')
            else:
                print(
                    f'{action_split[1]} is not found in the inventory of {indiana.name}. Try again.')

        else:
            print(f'{action_split[0]} is not a valid action. Try again.')
    else:

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

    elif action == 'i' or action == 'inventory':
        indiana.print_items()

    elif action == 'q':
        inPlay = False
