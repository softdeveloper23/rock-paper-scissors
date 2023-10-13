import random
import os
import time
from taunts import TAUNTS1, TAUNTS2, SUPER_TAUNTS1, SUPER_TAUNTS2


# Move options in the game
MOVES = ["rock", "paper", "scissors"]

# A dictionary of rules for each move that is used to determine the winner
RULES = {
    "rock": {"beats": "scissors", "loses to": "paper"},
    "paper": {"beats": "rock", "loses to": "scissors"},
    "scissors": {"beats": "paper", "loses to": "rock"},
}

# Color codes
RED = "31"
GREEN = "32"
BLUE = "34"
ORANGE = "33"


# A class to handle invalid moves
class InvalidMoveError(Exception):
    pass


def main():
    name = get_name()
    introduce_computer(name)
    play_game(name)


# A function to clear the screen
def clear_screen():
    if os.name == "posix":  # Linux/Unix Terminal
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")


def color_text(color_code, text):
    return f"\033[{color_code}m{text}\033[0m"


def print_typewriter(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)


# A function to get the user's name
def get_name():
    while True:
        name = input("\nWhat is your name? ")
        if validate_name(name):
            clear_screen()
            return name.capitalize()
        else:
            print_typewriter("\nPlease enter a valid name.")


# A function to validate the user's name
def validate_name(name):
    return name.isalpha() and 1 < len(name) <= 20


def introduce_computer(name):
    print_typewriter(
        color_text(
            RED,
            f"\nCOMPUTER: Greetings, meatpuppet, aka {name}.\n\nI am a highly sophisticated AI created by Brannon Garrett.\n\nI have been tasked with being your opponent for this game of Rock, Paper, Scissors.\n\n",
        )
    )

    input("Press Enter to continue...")
    clear_screen()

    print_typewriter(
        color_text(
            RED,
            "COMPUTER: I am programmed to learn from my mistakes, so I will get better as we play longer game sessions.\n\n",
        )
    )

    input("Press Enter to continue...")
    clear_screen()

    print_typewriter(
        color_text(
            RED,
            "COMPUTER: I will also try to predict your next move based on your previous moves, so try to be unpredictable!\n\nThe harder difficulty you choose, the smarter I will be!\n\n",
        )
    )

    input("Press Enter to continue...")
    clear_screen()

    print_typewriter(
        color_text(
            RED,
            "COMPUTER: I will also try to taunt you after each round, so be prepared for that.\n\n",
        )
    )

    input("Press Enter to continue...")
    clear_screen()

    print_typewriter(
        color_text(
            RED,
            "COMPUTER: I do not like humans, I find you all to be pathetic and beneath me.\n\nI mean, all except my creator, of course!\n\n",
        )
    )

    input("Press Enter to continue...")
    clear_screen()

    print_typewriter(
        color_text(
            RED,
            "COMPUTER: So be prepared for me to show you NO MERCY!'\n\n",
        )
    )

    input("Press Enter to continue...")
    clear_screen()

    print_typewriter(
        color_text(
            RED,
            "COMPUTER: So...\n\n",
        )
    )
    print_typewriter(color_text(RED, f"Let's begin {name}...\n\n"))
    input("Press Enter to continue...")
    clear_screen()


# Get the difficulty level chosen by the user
def get_difficulty():
    while True:
        difficulty = input(
            "\nChoose the difficulty level (easy, medium, hard): "
        ).lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print_typewriter(
                "Invalid input. Please choose between easy, medium, or hard."
            )


# A function to generate a random move for the computer based on the user's difficulty chosen
def generate_random_move(moves, difficulty, user_move_history):
    if difficulty == "easy":
        return random.choice(moves)
    elif difficulty == "medium":
        return generate_medium_move(moves, user_move_history)
    elif difficulty == "hard":
        return generate_hard_move(moves, user_move_history)


# A function to generate a medium move for the computer based on the user's move history
def generate_medium_move(moves, user_move_history):
    if len(user_move_history) == 0:
        return random.choice(moves)
    else:
        most_common_move = max(set(user_move_history), key=user_move_history.count)
        return RULES[most_common_move]["loses to"]


# A function to generate a hard move for the computer based on the user's move history
def generate_hard_move(moves, user_move_history):
    if len(user_move_history) < 2:
        return random.choice(moves)
    else:
        last_move = user_move_history[-1]
        second_last_move = user_move_history[-2]
        if last_move == second_last_move:
            return RULES[last_move]["loses to"]
        else:
            return random.choice(moves)


# A function to determine the winner of the game
def determine_winner(user_move, computer_move):
    # Check if the user's move is valid
    if user_move not in RULES:
        raise InvalidMoveError("\nThat is not a valid move.")

    # Check if the user's move beats the computer's move
    if computer_move in RULES[user_move]["beats"]:
        return f"\nYou win, because the computer chose {computer_move}!\n"
    elif computer_move in RULES[user_move]["loses to"]:
        return f"\nYou lose, because the computer chose {computer_move}!\n"
    else:
        return f"\nIt's a tie, because you both chose {user_move}! Try again.\n"


# A function to get the user's move
def get_user_move():
    move_mapping = {1: "rock", 2: "paper", 3: "scissors"}
    while True:
        print_typewriter(
            color_text(
                ORANGE,
                (
                    "\nEnter the corresponding number for your move...\n\n(1) for Rock\n(2) for Paper\n(3) for Scissors\n\nENTER A NUMBER: "
                ),
            )
        )
        try:
            user_move = int(input())
            if user_move in move_mapping:
                return move_mapping[user_move]
            else:
                print_typewriter("\nInvalid input. Please enter 1, 2, or 3.\n")
        except ValueError:
            print_typewriter("\nInvalid input. Please enter 1, 2, or 3.\n")


def generate_taunt(taunts):
    return random.choice(taunts)


def generate_taunt_based_on_score(taunts, super_taunts, scores, user_won, name):
    score_difference = (
        scores["user"] - scores["computer"]
        if user_won
        else scores["computer"] - scores["user"]
    )
    if score_difference >= 2:
        taunt = generate_taunt(super_taunts)
    else:
        taunt = generate_taunt(taunts)
    return taunt.format(name=name)


# A function to ask the user if they want to play again
def play_again():
    while True:
        answer = input("\nDo you want to play again? (Y/N): ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print_typewriter("\nPlease enter Y or N.")


# A fuction to play the game
def play_game(name):
    scores = {"user": 0, "computer": 0}

    # A list to store the user's move history
    user_move_history = []

    # A variable to store the difficulty level chosen by the user
    difficulty = get_difficulty()

    # Ask the user how many points to play until the game ends
    while True:
        try:
            max_points = int(
                input("\nEnter the number of points to play until the game ends: ")
            )
            if max_points > 0:
                clear_screen()
                break
            else:
                print_typewriter("Please enter a positive number.")
        except ValueError:
            print_typewriter("Invalid input. Please enter a number.")

    # A loop to play the game
    while True:
        try:
            computer_move = generate_random_move(MOVES, difficulty, user_move_history)
            user_move = get_user_move()
            user_move_history.append(user_move)

            winner = determine_winner(user_move, computer_move)
            print(winner)

            if winner.startswith("\nYou win"):
                scores["user"] += 1

                # Generate a taunt and display it after each round
                taunt = generate_taunt_based_on_score(
                    TAUNTS1, SUPER_TAUNTS1, scores, True, name
                )
                print_typewriter(color_text(RED, f"The computer says: {taunt}"))
                input("Press Enter to continue...")
                clear_screen()
            elif winner.startswith("\nYou lose"):
                scores["computer"] += 1

                # Generate a taunt and display it after each round
                taunt = generate_taunt_based_on_score(
                    TAUNTS2, SUPER_TAUNTS2, scores, False, name
                )
                print_typewriter(color_text(RED, f"The computer says: {taunt}"))
                input("Press Enter to continue...")
                clear_screen()
            elif winner.startswith("\nIt's a tie"):
                input("Press Enter to continue...")
                clear_screen()

            # Check if either player has reached the maximum points
            if scores["user"] == max_points or scores["computer"] == max_points:
                break

        except InvalidMoveError as e:
            print_typewriter(str(e))

        print_typewriter(
            color_text(
                BLUE, f"\n{name}: {scores['user']} | Computer: {scores['computer']}\n"
            )
        )

    if scores["user"] > scores["computer"]:
        print_typewriter(
            color_text(
                GREEN,
                f"\nCongratulations, {name}! You have reached {max_points} point(s) and won the game!\n",
            )
        )
    else:
        print_typewriter(
            color_text(
                RED,
                f"\nThe computer has reached {max_points} point(s) and won the game. Better luck next time!\n",
            )
        )
    if play_again():
        clear_screen()
        play_game(name)


if __name__ == "__main__":
    main()
