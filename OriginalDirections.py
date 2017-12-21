#motion = input("Would you like to enter the door to the north, south, east, or west? ").lower()

room = 1
def through_door():
    room1 = room
    motion = input("Would you like to enter the door to the north, south, east, or west? ").lower()
    if motion == 'north':
        room1 += 5
        print(f"You are now in room {room1}")
    elif motion == 'south':
        room1 -= 5
        print(f"You are now in room {room1}")
    elif motion == 'east':
        room1 += 1
        print(f"You are now in room {room1}")
    elif motion == 'west':
        room1 -= 1
        print(f"You are now in room {room1}")

print(through_door())