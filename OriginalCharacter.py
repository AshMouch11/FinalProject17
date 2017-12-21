name = input('What is your name? ')
room = 1

class Characters(object):
    def __init__(self, name, room):
        self.name = name
        self.room = room
character = Characters(name,room)
print(f"{character.name} is now in room {character.room}.")

room += 1
character = Characters(name,room)
print(f"{character.name} is now in room {character.room}.")
