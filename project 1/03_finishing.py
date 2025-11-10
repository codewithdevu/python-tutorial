import random

def play_game():
    # Computer randomly picks a number
    computer = random.choice([-1, 1, 0])
    yourstr = input("Enter your choice (st for stone, p for paper, si for scissor): ")
    
    yourdict = {"st": 1, "p": -1, "si": 0}
    reversedict = {1: "stone", -1: "paper", 0: "scissor"}

    # Input validation
    if yourstr not in yourdict:
        print("Invalid choice! Please enter 'st', 'p', or 'si'.")
        return

    you = yourdict[yourstr]

    print(f"You chose: {reversedict[you]}  \nComputer chose: {reversedict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif computer - you in [-2, 1]:
        print("You lose!")
    else:
        print("You win!")

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != 'yes':
        break
