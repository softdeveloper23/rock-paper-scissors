import random
import re

MOVES = ["rock", "paper", "scissors"]

RULES = {
    "rock": {"beats": "scissors", "loses to": "paper"},
    "paper": {"beats": "rock", "loses to": "scissors"},
    "scissors": {"beats": "paper", "loses to": "rock"},
}


class InvalidMoveError(Exception):
    pass


def main():
    name = get_name()
    play_game(name)


def get_name():
    while True:
        name = input("What is your name? ")
        if validate_name(name):
            return name.capitalize()
        else:
            print("Please enter a valid name.")


def validate_name(name):
    return name.isalpha() and 1 < len(name) <= 20


def generate_random_move(moves):
    return random.choice(moves)


def determine_winner(user_move, computer_move):
    if user_move not in RULES:
        raise InvalidMoveError("That is not a valid move.")

    if computer_move in RULES[user_move]["beats"]:
        return f"\nYou win, because the computer chose {computer_move}!"
    elif computer_move in RULES[user_move]["loses to"]:
        return f"\nYou lose, because the computer chose {computer_move}!"
    else:
        return f"\nIt's a tie, because you both chose {user_move}! Try again."


def get_user_move():
    while True:
        user_move = input("\nWhat is your move? (Rock, Paper, Scissors): ").lower()
        if user_move in MOVES:
            return user_move
        else:
            print("That is not a valid move.")


def play_again():
    while True:
        answer = input("\nDo you want to play again? (Y/N): ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter Y or N.")


def play_game(name):
    scores = {"user": 0, "computer": 0}

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

            if not play_again():
                break

        except InvalidMoveError as e:
            print(e)

    print(
        f"The final scores are:\nUser: {scores['user']}\nComputer: {scores['computer']}\n"
    )
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
