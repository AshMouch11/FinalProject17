name = input('What is your name? ')
room = 1
westendriddles = [6, 17, 28, 39, 50]
eastendriddles = [11, 22, 33, 44, 55]
southendriddles = [1, 2, 3, 4, 5]
northendriddles = [56, 57, 58, 59, 60]

class Characters(object):
    def __init__(self, name, room):
        self.name = name
        self.room = room
character = Characters(name,room)

def through_door():
    motion = input("Would you like to enter the door to the north, south, east, or west? ").lower()
    if motion == 'north':
        character.room += 5
        print(f"{character.name} is now in room {character.room}")
    elif motion == 'south':
        character.room -= 5
        print(f"{character.name} is now in room {character.room}")
    elif motion == 'east':
        character.room += 1
        print(f"{character.name} is now in room {character.room}")
    elif motion == 'west':
        character.room -= 1
        print(f"{character.name} is now in room {character.room}")
    else:
        print("Sorry, that is not an option.")
        print(through_door())


