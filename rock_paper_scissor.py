def rock_paper_scissor():
    print()
    print("This is 'Rock', 'Paper', 'Scissor' Game.")
    print()
    print("----------I N S T R U C T I O N----------")
    print()
    print("* Please enter the Integer number In-Front of the option.")
    print("* If you want to exit the game enter Zero '0'.")
    print()
    print("Enjoy the Game...")
    print()

    from random import randint

    game = {1:"Rock",2:"Paper",3:"Scissor"}

    score_p = 0
    score_c = 0
    esc = True
    name = input("Enter the player name : ")
    print()

    try:
        while esc:
            computer = game[randint(1,3)]
            for i,j in game.items():
                print(i," - ",j)

            player = int(input("Enter your Choice : "))

            if player == 0:
                esc = False
            elif game[player] == "Rock":
                if computer == "Rock":
                    print()
                    print("Tie.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_p += 1
                    score_c += 1
                elif computer == "Paper":
                    print()
                    print("You Loose.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_c += 1
                elif computer == "Scissor":
                    print()
                    print("You Win.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_p += 1
            elif game[player] == "Paper":
                if computer == "Rock":
                    print()
                    print("You Win.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_p += 1
                elif computer == "Paper":
                    print()
                    print("Tie.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_c += 1
                    score_p += 1
                elif computer == "Scissor":
                    print()
                    print("You Loose.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_c += 1
            elif game[player] == "Scissor":
                if computer == "Rock":
                    print()
                    print("You Loose.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_c += 1
                elif computer == "Paper":
                    print()
                    print("You Win.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_p += 1
                elif computer == "Scissor":
                    print()
                    print("Tie.....")
                    print(f"{name.capitalize()} - {game[player]} / Computer - {computer}")
                    print()
                    score_p += 1
                    score_c += 1

        if score_c > 0 and score_p > 0:
            if score_c > score_p:
                print()
                print(f"Computer wins the Game.")
                print(f"-----SCORES-----")
                print(f" - Computer = {score_c}")
                print(f" - {name.capitalize()} = {score_p}")
                print()
            elif score_p > score_c:
                print()
                print(f"{name.capitalize()} wins the Game.")
                print(f"-----SCORES-----")
                print(f" - Computer = {score_c}")
                print(f" - {name.capitalize()} = {score_p}")
                print()
            else:
                print()
                print(f"Tie......")
                print(f"-----SCORES-----")
                print(f" - Computer = {score_c}")
                print(f" - {name.capitalize()} = {score_p}")
                print()

    except KeyError:
        print()
        print("You're choice should between 1 to 3 (included).")
        if score_c > 0 and score_p > 0:
            print()
            print("-----SCORES-----")
            print(f" - {name.capitalize()} = {score_p}")
            print(f" - Computer = {score_c}")
        print()
        print("GAME ENDS ! ")

    except ValueError:
        print()
        print("You're choice should be an Integer between 1 to 3 (included).")
        if score_c > 0 and score_p > 0:
            print()
            print("-----SCORES-----")
            print(f" - {name.capitalize()} = {score_p}")
            print(f" - Computer = {score_c}")
        print()
        print("GAME ENDS ! ")

rock_paper_scissor()