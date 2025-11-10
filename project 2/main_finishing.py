import random

def play_game():
    n = random.randint(1, 100)
    a = -1
    guesses = 0

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100. Try to guess it!")

    while a != n:
        try:
            a = int(input("Guess the number: "))
            guesses += 1
            if a > n:
                print("Lower number please")
            elif a < n:
                print("Higher number please")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"\nCongratulations! You have guessed the number {n} correctly in {guesses} attempts.")

    # Provide feedback based on the number of attempts
    if guesses <= 5:
        print("Wow! You're a genius!")
    elif guesses <= 10:
        print("Good job! You did well.")
    else:
        print("You can do better next time.")

def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

# Start the game
main()
