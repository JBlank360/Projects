from random import randint
player_wins = 0
computer_wins = 0
winning_score = 5

print ("\nBest 5 out of 11")
while player_wins < winning_score and computer_wins < winning_score:
    print (f"\nPlayer score: {player_wins} Computer score: {computer_wins}")
    print ("\n...rock...")
    print ("...paper...")
    print ("...scissors...")

    player = input ("\nEnter your choice: ").lower()
    if player == "quit" or player == "q":
        break
    random_num = randint(0,2)
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"
    print(f"The computer plays: {computer}")



    if player == computer:
        print("\nI'ts a tie.")

    elif player == "rock":
        if computer == "paper":
            print ("\nComputer wins :(")
            computer_wins += 1
        else:
            print ("\nYou win!")
            player_wins += 1

    elif player == "paper":
        if computer == "scissors":
            print ("\nComputer wins :(")
            computer_wins += 1
        else:
            print ("\nYou win!")
            player_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print ("\nComputer wins :(")
            computer_wins += 1
        else:
            print ("\nYou win!")
            player_wins += 1
    else:
        print ("\nPlease enter a valid move.")

if player_wins > computer_wins:
    print ("Congrats, you won!")
else:
    print ("\nYou lost to a computer...")       
print (f"FINAL SCORES... \nPlayer:{player_wins} \nComputer: {computer_wins}")