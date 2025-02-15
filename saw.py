print()
print("You wake up confused about where you are or how you got there.", "\n")
print("You notice a dead body covered in blood in the middle of the floor with a gun and a tape recorder.", "\n")
print("There’s someone else in the room who is in the same position as you.", "\n")
print("You introduce yourselves to each other. One person is named Adam. The other is named Lawrence.", "\n")


while True:
    answer = input("Who do you want to play as?  (Adam or Lawrence?) ").lower().strip()

    if answer == "adam":
        print("You've chosen Adam.", "\n")
        print("You look down at the chains around your ankles and attempt to remove them.", "\n")
        answer = input("You hear Lawrence also strugling with his chains. Do you confront him?  (yes/no) ")
        if answer == "yes":
            print("You confront Lawrence about how you got here.", "\n")
            # answer = input("")

        elif answer == "no":
            print("You sit there in the room quietly and no one over finds you.", "\n", "You die. Game Over")
            break
        
        else:
            print("This is the room you die in because you failed to follow instructions.", "\n", "Game over.")
            break


    elif answer == "lawrence":
        print("You've chosed Lawrence.", "\n")


    else:
        print("This is the room you die in because you failed to choose someone.", "\n", "Game over.")
        break




# print("You both find an envelope in your pocket with your name on it. Inside, you find a tape with “PLAY ME” written on the outside.", "\n")