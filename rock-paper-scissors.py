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

    while True:
        if user_move in rules:
            break
        else:
            user_move = input("That is not a valid move. Please try again: ").lower()
    if user_move in rules and computer_move in rules[user_move]["beats"]:
        return "You win, because the computer chose " + computer_move + "!"
    elif user_move in rules and computer_move in rules[user_move]["loses to"]:
        return "You lose, because the computer chose " + computer_move + "!"
    elif user_move == computer_move:
        return "It's a tie, because you both chose " + user_move + "! Try again."
    else:
        return "I don't understand that!"


def play_game():
    moves = ["rock", "paper", "scissors"]
    scores = {"user": 0, "computer": 0}
    keep_playing = True

    while keep_playing:
        computer_move = generate_random_move(moves)
        user_move = input("What is your move? (Rock, Paper, Scissors): ").lower()
        winner = determine_winner(user_move, computer_move)
        print(winner)

        if winner.startswith("You win"):
            scores["user"] += 1
        elif winner.startswith("You lose"):
            scores["computer"] += 1
        else:
            pass

        keep_playing = input("Do you want to play again? (Y/N): ").lower() == "y"
    print(
        f"The final scores are: \nUser: {scores['user']} \nComputer: {scores['computer']} \n"
    )
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
