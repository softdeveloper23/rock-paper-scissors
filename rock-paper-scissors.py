import random
import os
import time


# Move options in the game
MOVES = ["rock", "paper", "scissors"]

# A dictionary of rules for each move that is used to determine the winner
RULES = {
    "rock": {"beats": "scissors", "loses to": "paper"},
    "paper": {"beats": "rock", "loses to": "scissors"},
    "scissors": {"beats": "paper", "loses to": "rock"},
}

TAUNTS1 = [
    "How did you win?\n\n",
    "That was pure luck!\n\n",
    "Are you cheating?\n\n",
    "Calculating next move...\n\n",
    "Unbelievable!\n\n",
]

TAUNTS2 = [
    "I know your next move...\n\n",
    "Is that all you've got?\n\n",
    "You're so predictable!\n\n",
    "I can read you like an open book!\n\n",
    "You'll have to do better than that!\n\n",
]


# A class to handle invalid moves
class InvalidMoveError(Exception):
    pass


def main():
    name = get_name()
    play_game(name)


# A function to clear the screen
def clear_screen():
    if os.name == "posix":  # Linux/Unix Terminal
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")


def print_typewriter(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)


# A function to get the user's name
def get_name():
    while True:
        name = input("\nWhat is your name? ")
        if validate_name(name):
            return name.capitalize()
        else:
            print_typewriter("\nPlease enter a valid name.")


# A function to validate the user's name
def validate_name(name):
    return name.isalpha() and 1 < len(name) <= 20


# Get the difficulty level chosen by the user
def get_difficulty():
    while True:
        difficulty = input("Choose the difficulty level (easy, medium, hard): ").lower()
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
        return f"\nIt's a tie, because you both chose {user_move}! Try again."


# A function to get the user's move
def get_user_move():
    while True:
        print_typewriter("\nWhat is your move? (Rock, Paper, Scissors): ")
        user_move = input().lower()
        if user_move in MOVES:
            return user_move
        else:
            print_typewriter("\nThat is not a valid move.")


def generate_taunt(taunts):
    return random.choice(taunts)


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
                input("Enter the number of points to play until the game ends: ")
            )
            if max_points > 0:
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
                taunt1 = generate_taunt(TAUNTS1)
                print_typewriter(taunt1)
                input("Press Enter to continue...")
                clear_screen()
            elif winner.startswith("\nYou lose"):
                scores["computer"] += 1

                # Generate a taunt and display it after each round
                taunt2 = generate_taunt(TAUNTS2)
                print_typewriter(taunt2)
                input("Press Enter to continue...")
                clear_screen()

            # Check if either player has reached the maximum points
            if scores["user"] == max_points or scores["computer"] == max_points:
                break

        except InvalidMoveError as e:
            print_typewriter(str(e))

        print_typewriter(f"\n{name}: {scores['user']} | Computer: {scores['computer']}")

    if scores["user"] > scores["computer"]:
        print_typewriter(
            f"\nCongratulations, {name}! You have reached {max_points} points and won the game!"
        )
    else:
        print_typewriter(
            f"\nThe computer has reached {max_points} points and won the game. Better luck next time!"
        )


if __name__ == "__main__":
    main()
