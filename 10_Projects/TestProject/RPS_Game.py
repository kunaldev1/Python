import random


def get_user_choice():
    """
    Prompts the user to enter their choice of rock, paper, or scissors.

    Returns:
        str: The user's choice.
    """
    while True:
        user = input("Enter rock, paper, or scissors: ").lower()
        if user in ["rock", "paper", "scissors"]:
            return user
        else:
            print("Invalid input. Please enter rock, paper, or scissors!!!")


def get_computer_choice():
    """
    Returns a random choice of rock, paper, or scissors.

    Returns:
        str: The computer's choice.
    """
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the Rock-Paper-Scissors game.

    Args:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.

    Returns:
        str: The result of the game (win, tie, or loss).
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_rps_game():
    """
    Plays the Rock-Paper-Scissors game.
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer chooses:", computer_choice)
    print(determine_winner(user_choice, computer_choice))


if __name__ == "__main__":
    play_rps_game()
