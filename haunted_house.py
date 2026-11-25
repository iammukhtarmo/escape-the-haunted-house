
while True:
    print("\nWelcome to Escape the Haunted House!")
    print("You wake up inside a dark mansion.")
    print("Your mission is to escape alive.")

    # STAGE 1: CHOOSE A PATH
    while True:
        choice1 = input("Choose basement or upstairs?\n").strip().lower()

        if choice1 == "basement":
            print("You found a mysterious room.")
            break

        elif choice1 == "upstairs":
            print("A ghost catches you. Game Over.")
            break

        else:
            print("Invalid choice! Choose basement or upstairs.")

    if choice1 == "basement":

        # STAGE 2: CHOOSE AN OBJECT
        while True:
            choice2 = input("Choose key or flashlight?\n").strip().lower()

            if choice2 == "key":
                print("You opened the locked door.")
                break

            elif choice2 == "flashlight":
                print("A monster attacks you. Game Over.")
                break

            else:
                print("Invalid choice! Choose key or flashlight.")

        if choice2 == "key":

            # STAGE 3: CHOOSE A DOOR
            while True:
                choice3 = input("Choose Red, Blue or Green?\n").strip().lower()

                if choice3 == "red":
                    print("You are trapped in a fire. Game Over.")
                    break

                elif choice3 == "blue":
                    print("You are safe to pass.")
                    break

                elif choice3 == "green":
                    print("The room is locked. Game Over.")
                    break

                else:
                    print("Invalid choice! Choose Red, Blue or Green.")

            if choice3 == "blue":

                # STAGE 4: FINAL ESCAPE
                while True:
                    choice4 = input("Do you want to run or hide?\n").strip().lower()

                    if choice4 == "run":
                        print("Congratulations! You escaped the haunted house!")
                        break

                    elif choice4 == "hide":
                        print("A ghost finds you. Game Over.")
                        break

                    else:
                        print("Invalid choice! Choose run or hide.")

    # RESTART THE GAME
    while True:
        restart = input("Would you like to play again? yes/no\n").strip().lower()

        if restart in ("yes", "y"):
            print("Restarting the game...")
            break

        elif restart in ("no", "n"):
            print("Thanks for playing Escape the Haunted House!")
            break

        else:
            print("Invalid choice! Please enter yes or no.")

    if restart in ("no", "n"):
        break