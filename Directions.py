questions = input("Welcome to Ash's super amazing junior year final programming project! Before I explain to you the rules of the game, would you prefer to be asked questions about : Supernatural (the TV show), Math, or Sherlock (the TV show)? ")
print(f"{questions}? Awesome. Get ready for some great questions about {questions}.")
directions = """You have just been dropped into the 5x5 grid of rooms pictured below, in order to escape you need to find the randomly assigned door that allows you to flee.
Each room has 4 doors, labeled north, south, east, and west, and besides the escape door, each door will lead you to the next room.
In order to get through the door, however, you will need to answer a question about the topic you just chose.
You will have 3 attempts to answer this question or the door will be locked forever.
If you lock the escape door, you LOSE.
Good luck!
--------------------------
| 20 | 21 | 22 | 23 | 24 |
--------------------------
| 15 | 16 | 17 | 18 | 19 |
--------------------------
| 10 | 11 | 12 | 13 | 14 |
--------------------------
| 5  | 6  | 7  | 8  | 9  |
--------------------------
| 0  | 1  | 2  | 3  | 4  |
--------------------------"""
print(directions)