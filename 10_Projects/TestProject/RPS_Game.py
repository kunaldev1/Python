"""Interactive Rock-Paper-Scissors game."""

import random

CHOICES = ("rock", "paper", "scissors")


def get_user_choice():
    """Prompt until the user enters rock, paper, or scissors."""
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if user_choice in CHOICES:
            return user_choice
        print("Invalid input. Please enter rock, paper, or scissors.")


def get_computer_choice():
    """Return a random valid choice for the computer."""
    return random.choice(CHOICES)


def determine_winner(user_choice, computer_choice):
    """Return the outcome message for two valid game choices.

    Raises:
        ValueError: If either choice is not rock, paper, or scissors.
    """
    if user_choice not in CHOICES or computer_choice not in CHOICES:
        raise ValueError(f"Choices must be one of: {', '.join(CHOICES)}")

    if user_choice == computer_choice:
        return "It's a tie!"

    user_wins = (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    )
    return "You win!" if user_wins else "Computer wins!"


def play_rps_game():
    """Play one round of Rock-Paper-Scissors and print the result."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer chooses:", computer_choice)
    print(determine_winner(user_choice, computer_choice))


if __name__ == "__main__":
    play_rps_game()
