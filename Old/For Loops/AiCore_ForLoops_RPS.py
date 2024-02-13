
player_1_wins = 0
player_2_wins = 0

while player_1_wins < 3 and player_2_wins < 3:
    player_1 = input("What is player 1 choice? rock, paper or scissors? ")
    player_2 = input("What is player 2 choice? rock, paper or scissors? ")

    choices = ("rock", "paper", "scissors")

# TODO - Code the logic for the game
    if player_1 and player_2 not in choices:
        print("Wrong Inputs")
    elif player_1 == player_2:
        print("Draw") 

    #if player 1 selects rock and player 2 selects scissors
    elif player_1 == "rock":
        if player_2 == "scissors":
            print('Player 1 wins')
            player_1_wins += 1
        else:
            print('Player 2 wins')
            player_2_wins += 1

    #if player 1 selects scissors and player 2 selects paper
    elif player_1 == "scissors":
        if player_2 == "paper":
            print('Player 1 wins')
            player_1_wins += 1

        else:
            print('Player 2 wins')
            player_2_wins += 1

    #if player 1 selects paper and player 2 selects rock
    elif player_1 == "paper":
        if player_2 == "rock":
            print('Player 1 wins')
            player_1_wins += 1
        else:
           print('Player 2 wins')
           player_2_wins += 1

print(f"Player 1 won {player_1_wins} times")
print(f"Player 2 won {player_2_wins}")