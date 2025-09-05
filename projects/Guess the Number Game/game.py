import random


def guess_the_number():
    """
    This function runs the 'Guess the Number' game.
    """
    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    # Greet the player and explain the rules
    print("🎉 Welcome to the Guess the Number Game! 🎉")
    print("I'm thinking of a number between 1 and 100.")

    # Main game loop
    while True:
        try:
            # Prompt the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempt counter

            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low! Try again. 👇")
            elif guess > secret_number:
                print("Too high! Try again. 👆")
            else:
                print(f"🥳 Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts. Well done!")
                break  # Exit the loop since the game is won

        except ValueError:
            # Handle cases where the input is not a valid number
            print("Invalid input. Please enter a whole number. 🧐")


# Start the game
if __name__ == "__main__":
    guess_the_number()