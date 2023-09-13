import random
import re

# Move options in the game
MOVES = ["rock", "paper", "scissors"]

# A dictionary of rules for each move that is used to determine the winner
RULES = {
    "rock": {"beats": "scissors", "loses to": "paper"},
    "paper": {"beats": "rock", "loses to": "scissors"},
    "scissors": {"beats": "paper", "loses to": "rock"},
}


# A class to handle invalid moves
class InvalidMoveError(Exception):
    pass


def main():
    name = get_name()
    play_game(name)


# A function to get the user's name
def get_name():
    while True:
        name = input("\nWhat is your name? ")
        if validate_name(name):
            return name.capitalize()
        else:
            print("\nPlease enter a valid name.")


# A function to validate the user's name
def validate_name(name):
    return name.isalpha() and 1 < len(name) <= 20


# A function to generate a random move for the computer
def generate_random_move(moves):
    return random.choice(moves)


# A function to determine the winner of the game
def determine_winner(user_move, computer_move):
    # Check if the user's move is valid
    if user_move not in RULES:
        raise InvalidMoveError("\nThat is not a valid move.")

    # Check if the user's move beats the computer's move
    if computer_move in RULES[user_move]["beats"]:
        return f"\nYou win, because the computer chose {computer_move}!"
    elif computer_move in RULES[user_move]["loses to"]:
        return f"\nYou lose, because the computer chose {computer_move}!"
    else:
        return f"\nIt's a tie, because you both chose {user_move}! Try again."


# A function to get the user's move
def get_user_move():
    while True:
        user_move = input("\nWhat is your move? (Rock, Paper, Scissors): ").lower()
        if user_move in MOVES:
            return user_move
        else:
            print("\nThat is not a valid move.")


# A function to ask the user if they want to play again
def play_again():
    while True:
        answer = input("\nDo you want to play again? (Y/N): ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("\nPlease enter Y or N.")


# A function to play the game
def play_game(name):
    scores = {"user": 0, "computer": 0}

    # Ask the user how many points to play until the game ends
    while True:
        try:
            max_points = int(
                input("\nEnter the number of points to play until the game ends: ")
            )
            if max_points > 0:
                break
            else:
                print("\nPlease enter a positive number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

    # Play the game until either player reaches the maximum points
    while True:
        try:
            computer_move = generate_random_move(MOVES)
            user_move = get_user_move()

            winner = determine_winner(user_move, computer_move)
            print(winner)

            if winner.startswith("\nYou win"):
                scores["user"] += 1
            elif winner.startswith("\nYou lose"):
                scores["computer"] += 1

            # Check if either player has reached the maximum points
            if scores["user"] == max_points or scores["computer"] == max_points:
                break

        except InvalidMoveError as e:
            print(e)

    print(
        f"\nThe final scores are:\nUser: {scores['user']}\nComputer: {scores['computer']}\n"
    )
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
