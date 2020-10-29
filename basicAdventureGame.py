import time

# if game is true then the game plays but if user wants to quit than game is set to false.
game = True

# start of the game by asking user if they want to play.
print("Welcome to Choice adventure game!")
time.sleep(0.5)
askToPlay = input("Do you wanna play? (yes/no) : ")

while game == True:
    # checks is user wants to play then initiates the game.
    if askToPlay.lower() == "yes":
        game = True
    elif askToPlay.lower() == "no":
        game = False
        print("Ok have a good one.")
        break
    else:
        game = False
        print("Im sorry i misunderstood please try again.")
        break

    print("Okay! let's get started!")
    time.sleep(0.45)
    print("")

    firstStage = input("You are in a dark forest, but you see a small fire fade ahead of you.\nYou also hear water to the left of you. Where do you decide to go? (Straight/Left) : ")
    print("")

    # checks to see if user took the route towards the water
    def waterRoute():
        print("You head down towards the water.")
        time.sleep(0.3)
        print("You then hear ruffling behind you")
        time.sleep(0.3)
        print("AHHHHHHH")
        time.sleep(0.5)
        print("Someone hit you with a rock and you fell in.")
        print("END GAME")

    if firstStage.lower() == "straight":
        print("You went straight, towards the fire.")
        secondStage = input("You see a house, it's a log cabin. Do you go in or double back towards the water? (In/Water) : ")
    elif firstStage.lower() == "left":
        waterRoute()
        game = False
        break
    else:
        print("Invalid Answer")
        game = False
        break

    print("")

    if secondStage.lower() == "in":
        thirdStage = input("You go into the log cabin. Theres a door to the right of you, its cracked open but its dark and you cant see\ninside. Now do you want to go to the right towards the door or walk out and find another route? (Right/Turn Back) : ")
    elif secondStage.lower() == "water":
        waterRoute()
        game = False
        break
    else:
        print("Invalid Answer")
        game = False
        break

    if thirdStage.lower() == "right":
        print("")
        print("You open the the door, it's loud a creaky...")
        time.sleep(1)
        print("AHHH")
        time.sleep(0.5)
        print("Someone stabs you in the back and you die")
        print("END GAME")
    elif thirdStage.lower() == "turn back":
        print("")
        time.sleep(1)
        print("You head out the door but you hear something run up from behind you. You turn around...")
        time.sleep(1)
        print("h.. h.. hel... help m... me")
        print("Someone drives a axe into your neck and you die")
        print("END GAME")
        game = False
        break
    break