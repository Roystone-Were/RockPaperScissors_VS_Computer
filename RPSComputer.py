from random import randint
print("...WELCOME T0...")
print("...ROCK...")
print("...PAPER...")
print("...SCISSOR...")

player = input("Take Your move:\n").lower() #input().lower lowecases Uppercase characters

randomNumber = randint(0,2) # randint() give random numbers between 0 and 2 inclusive
if randomNumber == 0: 
    computer = "rock" # 0 == "rock"
elif randomNumber == 1:
    computer = "paper" #1 == "paper"
else:
    computer = "scissors" #2 == "scissors"

print(f"Your opponent played {computer}")


if player == computer:
    print("IT'S A DRAW")

# Rock Conditions
elif player == "rock":
    if computer == "scissors":
        print("You WIN")
    elif computer == "paper":
        print("You lost")

#Paper Conditions
elif player == "paper":
    if computer == "scissors":
        print("You Lost")
    elif computer == "rock":
        print("You WIN")
        
#Scissors Conditions
elif player == "scissors":
    if computer == "rock":
        print("You lost")
    elif computer == "paper":
        print("You WIN")

    
else:
    print("ERROR enter valid move")



