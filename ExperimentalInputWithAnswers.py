riddle1 = """   Which of the following is the same as the expression sin(x-y)cosy + cos(x-y)siny?
a. 1
b. sinx
c. cosx
d. sinxcos2y
"""

answer1 = 'b'

door1 = {'riddle' : riddle1 , 'answer' : answer1 , 'status' : 'locked'}

#MAKE THIS GENERALIZED DUMBASS

current_riddle = character.room[motion]['riddle']




def riddle_quiz():
    x=1
    response = input(f"{current_riddle}").lower()
    while True:
        if response == current_door['answer']:
            print("Correct. This door is now unlocked.")
            current_door['status'] = 'unlocked'
            break
        elif x>=3:
            print("This door is now locked forever.")
            current_door['status'] = 'permanently locked'
            break
        else:
            print(f"Incorrect. You now have {3-x} tries before this door is locked forever.")
            response = input(f"{current_riddle}").lower()
            x += 1

riddle_quiz()
print(current_door)