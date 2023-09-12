import random


def main():
    play_game()


def generate_random_move(moves):
    return random.choice(moves)


def determine_winner(user_move, computer_move):
    rules = {
        "rock": {"beats": "scissors", "loses to": "paper"},
        "paper": {"beats": "rock", "loses to": "scissors"},
        "scissors": {"beats": "paper", "loses to": "rock"},
    }

    if user_move in rules and computer_move in rules[user_move]["beats"]:
        return "You win!"
    elif user_move in rules and computer_move in rules[user_move]["loses to"]:
        return "You lose!"
    elif user_move == computer_move:
        return "It's a tie!"
    else:
        return "I don't understand that!"


def play_game():
    moves = ["rock", "paper", "scissors"]
    scores = {"user": 0, "computer": 0}
    keep_playing = True

    while keep_playing:
        computer_move = generate_random_move(moves)
        user_move = input("What is your move? (Rock, Paper, Scissors): ").lower()
        print(f"The computer chose {computer_move}.")
        print(determine_winner(user_move, computer_move))

        keep_playing = input("Do you want to play again? (Y/N): ").lower() == "y"


if __name__ == "__main__":
    main()
