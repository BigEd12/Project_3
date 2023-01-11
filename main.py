print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

q1 = input("You come to a fork in the path, which way do you want to go? Type 'left' or 'right'.")

q1_lc = q1.lower()

if q1_lc == "right":
    print(
        "You turned right and in the dark you didn't notice what was up ahead...\nGAME OVER! You fell down a hole and died!")
else:
    print("You followed the left path and eventually arrive at a river.")
    q2 = input(
        "At the river you see a sign that says there is a boat crossing. You don't know when the boat will arrive. What do you want to do? Type 'swim' or 'wait'.")

    q2_lc = q2.lower()

    if q2_lc == "swim":
        print(
            "Game over! The river is full of hungry trout that have developed a taste for human flesh.\nThat was a bad move, wasn't it?")
    else:
        print(
            "After what feels like hours, you see a boat on the horizon. When it arrives you climb aboard and the captain tells you about man-eating trout. You're glad you waited!")
        q3 = input(
            "You make it to the other side of the river and see a turret. The last reamining ruins of an old castle.\nAs you approach it you see there are three doors, all of different colours, red, blue or yellow.\nWhich door will you take? Type 'red', 'blue' or 'yellow'.")

        q3_lc = q3.lower()
        if q3_lc == "red":
            print(
                "Game over!\nThe room is on fire. As soon as you open the door, your nose hairs are singed and your skin melts of your bones.")
        elif q3_lc == "blue":
            print("Game over!\nThis room is full of water. As you open the door a tsunami envelopes you and you drown.")
        elif q3_lc == "yellow":
            print("Congratulations! The whole room is glinting in the warm glow of sun striking gold.")
        else:
            print("That wasn't an option. You died due to being thick.")