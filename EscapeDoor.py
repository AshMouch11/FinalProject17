import random
escape_door = random.randrang(1,50)

if roomcounter == rooms[escape_door]:
    escape_room_code()


def escape_room_code(motion):
    print("Congratulations! You have found the final door, after probably wandering around aimlessly and wasting your afternoon. This is the final question. If you get this question wrong, you lose, and the time spent playing this spectacular program that definitely deserves a 100% will truly be wasted. Good luck; you only have one try.")
    current_riddle = rooms[roomcounter][motion]['riddle']
    response = input(f"{current_riddle}").lower()
    if response == current_door['answer']:
            print("CONGRATULATIONS! YOU BEAT THE GAME. WONDERFUL JOB.")
            break
    else:
            print("Wow, really. The last question and you manage to get it wrong. I am a little disappointed. Now you can either play again or go and thing about what you've done.")
            print("YOU LOSE.")
            break