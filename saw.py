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
        answer = input("You hear Lawrence also strugling with his chains. Do you confront him?  (yes/no) ").lower().strip()
        if answer == "yes":
            print("You confront Lawrence about how you got here.", "\n")
            print("Lawrence notices a clock on the wall that looks brand new.", "\n")
            print("You find an envelope in your pocket with your name on it. Inside, it contains a tape with PLAY ME written on the outside", "\n")
            print("Lawrence also finds an envelope with a tape but his also contains a key", "\n")
            print("Lawrence tried the key on both locks holding the chain around his ankle, but the key works for neither lock.", "\n")
            answer = input("Do you ask Lawrence to throw you the key?  (yes/no) ").lower().strip()
            if answer == "yes":
                print("Lawrence throws you the key and you try it on both locks, but the key works for neither lock.", "\n")
                # print("")


            elif answer == "no":
                print("You sit there in the room quietly and no one over finds you.", "\n", "You die. Game Over")
                break


            else:
                print("This is the room you die in because you failed to follow instructions.", "\n", "Game over.")
                break


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