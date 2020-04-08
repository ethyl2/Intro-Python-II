from room import Room
from player import Player
from item import Item, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east, and west.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),

    'lake_room': Room("Underground Lake Chamber", """In the middle of the large chamber is
a deep, dark lake. If you hug the edges of the room as you walk, you should be able to make it 
across the chamber. If not, it's time to swim! The chamber has a exit to the west and north.""", False),

    'bone_pit': Room("Pit of Bones", """This depressing room is littered with scattered bones.
Looks like a dead end, in more ways than one.""", False),

    'cathedral': Room("Grand Cathedral", """The ceiling soars high above you. A few skylights let in
a few distinct rays of light. Inside this cavern are some of the most beautiful formations you've ever 
seen, including a large stalagmite forest and a 'frozen' waterfall. You gaze in awe for a while; 
unfortunately, it looks like the only practical way out is the way you came in.""", True)
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

"""Items"""

# Regular Items

necklace = Item('necklace', '📿 a sparkly string of interesting gems')
ring = Item('ring', '💍 engraved in an unknown language')
broom = Item('broom', '🧹 falling apart from much use')
spider = Item('spider', '🕷️  a long-legged fuzzy creature')
coins = Item('coins', '💰 contained in a convenient bag')
dagger = Item(
    'dagger', '🗡️  a pointed knife with a steel blade, handy for thrusting in close combat')
pick = Item(
    'pick', '⛏️  a tool with a curved spike for breaking up rocks in mining')

# LightSources

candle = LightSource('candle', '🕯️ almost burnt down to nothing')
lantern = LightSource('lantern', '🏮 handy for exploring dark places')
flashlight = LightSource(
    'flashlight', '🔦 luckily for you, still has working 🔋 batteries')

"""Add Items to Rooms"""

room['outside'].add_item(broom)
room['outside'].add_item(candle)
room['treasure'].add_item(spider)
room['foyer'].add_item(ring)
room['foyer'].add_item(necklace)
room['lake_room'].add_item(lantern)
room['overlook'].add_item(flashlight)
room['cathedral'].add_item(coins)
room['bone_pit'].add_item(dagger)
room['cathedral'].add_item(pick)

"""Add Riddles"""
room['lake_room'].add_question(
    'I live in the water, but never get wet. What am I? (in one word)')
room['lake_room'].add_answer('reflection')

room['treasure'].add_question(
    "If you have me, you want to share me. If you share me, you haven't got me. What am I? (in one word)")
room['treasure'].add_answer('secret')

room['narrow'].add_question(
    "I can travel around the world while staying in a corner. What am I? (in one word)")
room['narrow'].add_answer('stamp')

room['bone_pit'].add_question(
    "I am easy to get into, but hard to get out of. What am I? (in one word)")
room['bone_pit'].add_answer('trouble')

room['overlook'].add_question(
    "I fly without wings and cry without eyes. What am I? (in one word)")
room['overlook'].add_answer('cloud')

room['cathedral'].add_question("""I am a ship that can be made to ride the greatest waves. 
I am not built by tool, but built by hearts and minds. What am I? (in one word)""")
room['cathedral'].add_answer('friendship')

room['foyer'].add_question(
    "What word is spelled wrong in all the dictionaries?")
room['foyer'].add_answer('wrong')

room['outside'].add_question(
    "What gets bigger and bigger the more you take away from it? (one word)")
room['outside'].add_answer('hole')


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
    return f"\033[1;31;40m {indiana.name} can't go {directions[action]}. Make another choice."


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


"""
Modify the main loop to test if there is light in the Room 
(i.e. if is_light is True or there is a LightSource item in the Room's contents 
or if there is a LightSource item in the Player's contents).

Hint: isinstance might help you figure out if there's a LightSource among all the nearby Items.
"""


def light_check(room, player):
    has_light = False
    if room.is_light == True or [
            x for x in room.items if isinstance(x, LightSource)] or [
            x for x in player.items if isinstance(x, LightSource)]:
        has_light = True
    return has_light


"""
Modify the get/take code to print "Good luck finding that in the dark!" 
if the user tries to pick up an Item in the dark.
"""

inPlay = True
while inPlay:
    if light_check(indiana.current_room, indiana):
        print(indiana)
        indiana.current_room.print_items()
    else:
        print("\033[1;36;40m It's pitch black!")
    indiana.current_room.print_question()
    action = input(
        f"\033[0;35;40m Choose one: go [n] north, [s] south, [e] east, [w] west, [i] show inventory, [q] quit OR type 'get [item]' OR 'drop [item]'.\n \033[m")

    action_split = action.split(' ')
    if len(action_split) == 2:
        if action_split[0] == 'get' or action_split[0] == 'take':
            matches = [
                x for x in indiana.current_room.items if x.name == action_split[1]]

            if len(matches) > 0:
                if not light_check(indiana.current_room, indiana):
                    print("\033[1;36;40m Good luck finding that in the dark!")
                indiana.current_room.remove_item(matches[0])
                indiana.add_item(matches[0])
                matches[0].on_take(indiana.name, 'has')
            else:
                print(
                    f'\033[1;31;40m {action_split[1]} is not found in the {indiana.current_room.name}. Try again.')
        elif action_split[0] == 'drop':
            matches = [
                x for x in indiana.items if x.name == action_split[1]]
            if len(matches) > 0:
                indiana.current_room.add_item(matches[0])
                indiana.remove_item(matches[0])
                matches[0].on_drop(indiana.name, 'has')
            else:
                print(
                    f'\033[1;31;40m {action_split[1]} is not found in the inventory of {indiana.name}. Try again.')

        else:
            print(
                f'\033[1;31;40m {action_split[0]} is not a valid action. Try again.')
    else:

        if action not in directions.keys():
            print(f'\033[1;31;40m {action} is an invalid choice. Try again.')
        else:
            print(
                f'\033[0;33;40m \n{indiana.name} wants to go {directions[action]}.')

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
