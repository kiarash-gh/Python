import random

print("**********          Rock, Paper and Scissor game          **********")
print("____________________________________________________________________")
print("""
input r for Rock
input p for paper
input s for scissor
""")
print("____________________________________________________________________")

choices = ["ROCK","PAPER",'SCISSORS']

player_name = input("Please Enter Your Name: ").title()
print("Hi {}".format(player_name))
set_rounds = int(input("How Many Rounds would You Like To Play? "))

rounds = 0
player_score = 0
computer_score = 0

while rounds < set_rounds:

    print("Round {}".format(rounds + 1))
    

    computer = random.choice(choices)

    player =input("ROCK, PAPER OR SCISSORS?  " ).upper()
    
    print("computer's choice: " ,computer)
    
    if player == "R" or player == "ROCK":
        if computer == "ROCK":
            print("Tie!")
        elif computer == "PAPER":
            print("You Lose! {} Covers ROCK".format(computer))
            computer_score += 1
        elif computer == "SCISSORS":
            print("You Win! ROCK Smashes {}".format(computer))
            player_score += 1
    
    elif player == "P" or player == "PAPER":
        if computer == "ROCK":
            print("You Win! PAPER Covers {}".format(computer))
            player_score += 1
        elif computer == "PAPER":
            print("Tie!")
        elif computer == "SCISSORS":
            print("You Lose! {} Cut PAPER".format(computer))
            computer_score += 1

    elif player == "S" or player == "SCISSORS":
        if computer == "ROCK":
            print("You Lose! {} Smashes SCISSORS".format(computer))
            computer_score += 1
        elif computer == "PAPER":
            print("You Win! SCISSORS Cut {}".format(computer))
            player_score += 1
        elif computer == "SCISSORS":
            print("Tie!") 

    print(" ")
    print("{}'s Score: {}".format(player_name, player_score))
    print("Computer's Score: {}".format(computer_score))
    print(" ")
    print("***********************************************")
    print(" ")
    
    rounds += 1

print("___________________________________________________")
print("**********          Final Score          **********")
print("{}'s Score: {}".format(player_name, player_score))
print("Computer's Score: {}".format(computer_score))
if computer_score == player_score:
    print("Tie")  
elif computer_score < player_score:
    print("You Won By {} Points :)".format(player_score - computer_score))
else:
    print("You Lost By {} Points :(".format(computer_score - player_score))

print("Thank You For Playing.")
print("GoodBye")
print("___________________________________________________")