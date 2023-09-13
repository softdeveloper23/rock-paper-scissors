import random
import re
import time
import tkinter as tk


# This is a simple rock, paper, scissors game.
def main():
    # Run the game
    play_game()


# This function generates a random move for the computer
def generate_random_move(moves):
    return random.choice(moves)


# This function determines the winner of the game
def determine_winner(user_move, computer_move):
    # These are the rules of the game
    rules = {
        "rock": {"beats": "scissors", "loses to": "paper"},
        "paper": {"beats": "rock", "loses to": "scissors"},
        "scissors": {"beats": "paper", "loses to": "rock"},
    }

    # This checks if the user's move is valid
    if user_move not in rules:
        return "\nThat is not a valid move."

    # This checks if the user won, lost, or tied
    if user_move in rules and computer_move in rules[user_move]["beats"]:
        return "\nYou win, because the computer chose " + computer_move + "!"
    elif user_move in rules and computer_move in rules[user_move]["loses to"]:
        return "\nYou lose, because the computer chose " + computer_move + "!"
    elif user_move == computer_move:
        return "\nIt's a tie, because you both chose " + user_move + "! Try again."


# This function runs the game
def play_game():
    # Stores the moves in a list
    moves = ["rock", "paper", "scissors"]

    # Stores the scores in a dictionary
    scores = {"user": 0, "computer": 0}

    # This variable keeps track of whether the user wants to keep playing
    keep_playing = True

    # This variable stores the user's name
    name = ""
    while True:
        name = input("What is your name? ")
        if not validate_name(name):
            print("Please enter a valid name.")
        else:
            break
    name = name.capitalize()
    print(f"\nHi {name}! Let's play Rock, Paper, Scissors!")

    # This loop runs the game until the user doesn't want to play anymore
    while keep_playing:
        computer_move = generate_random_move(moves)
        user_move = input("\nWhat is your move? (Rock, Paper, Scissors): ").lower()

        # This passes the moves to the determine_winner function which returns the winner
        winner = determine_winner(user_move, computer_move)
        print(winner)

        # This updates the scores
        if winner.startswith("\nYou win"):
            scores["user"] += 1
        elif winner.startswith("\nYou lose"):
            scores["computer"] += 1
        else:
            pass

        keep_playing = input("\nDo you want to play again? (Y/N): ").lower() == "y"

    print(
        f"The final scores are: \nUser: {scores['user']} \nComputer: {scores['computer']} \n"
    )
    print("Thanks for playing!")


# This function validates the user's name
def validate_name(name):
    regex = "^[a-zA-Z]+$"
    match = re.match(regex, name)

    if match and len(name) > 1 and len(name) <= 20:
        return True
    else:
        name = ""
        return False


if __name__ == "__main__":
    main()
