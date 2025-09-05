import random


def get_computer_choice():
    """Randomly returns 'rock', 'paper', or 'scissors'."""
    return random.choice(['rock', 'paper', 'scissors'])


def get_winner(player_choice, computer_choice):
    """Determines the winner based on game rules."""
    if player_choice == computer_choice:
        return "It's a tie! 🤝"

    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if winning_combinations[player_choice] == computer_choice:
        return "You win! 🎉"
    else:
        return "You lose! 😢"


def play_game():
    """Main function to play the Rock, Paper, Scissors game."""
    print("--- Rock, Paper, Scissors ---")

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYour choice: {player_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")

        result = get_winner(player_choice, computer_choice)
        print(result)

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! 👋")
            break
        print("-" * 20)


if __name__ == "__main__":
    play_game()