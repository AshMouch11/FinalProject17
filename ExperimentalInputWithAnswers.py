riddle1 = """   Which of the following is the same as the expression sin(x-y)cosy + cos(x-y)siny?
a. 1
b. sinx
c. cosx
d. sinxcos2y
"""

answer1 = 'b'

response = input(f"{riddle1}").lower()
x=1
while True:
    if response == answer1:
        print("Correct. This door is now unlocked.")
        break
    elif x>=3:
        print("This door is now locked forever.")
        # INSERT SOMETHING THAT LOCKS THE DOOR DUMBASS
        break
    else:
        print(f"Incorrect. You now have {3-x} tries before this door is locked forever.")
        response = input(f"{riddle1}").lower()
        x += 1
