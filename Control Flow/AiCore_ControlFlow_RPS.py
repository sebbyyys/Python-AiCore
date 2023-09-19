player_1 = input("What is player 1 choice? rock, paper or scissors? ")
player_2 = input("What is player 2 choice? rock, paper or scissors? ")
# Add your code below this line

choices = ("rock", "paper", "scissors")
   
if player_1 and player_2 not in choices:
    print("Wrong Inputs")
elif player_1 == player_2:
    print("Draw") 

    #if player 1 selects rock and player 2 selects scissors
elif player_1 == "rock":
    if player_2 == "scissors":
            print("Player 1 Rock beats Player 2 Scissors")
    else:
          print("Player 1 Rock loses to Player 2 Paper")



    #if player 1 selects scissors and player 2 selects paper
elif player_1 == "scissors":
    if player_2 == "paper":
            print("Player 1 Scissors beats Player 2 Paper")
    else:
            print("Player 1 Scissors loses to Player 2 Rock")

#if player 1 selects paper and player 2 selects rock
            
elif player_1 == "paper":
    if player_2 == "rock":
            print("Player 1 Paper beats Player 2 Rock")
    else:
           print("Player 1 Paper loses to Player 2 Scissors")
