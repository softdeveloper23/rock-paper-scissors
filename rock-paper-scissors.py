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

# Color codes
RED = "31"
GREEN = "32"
BLUE = "34"
ORANGE = "33"

TAUNTS1 = [
    "'How did you win? No, really, HOW???'\n\n",
    "'That was pure luck! And I think your luck is about to run out...'\n\n",
    "'Are you cheating? You're cheating aren't you?'\n\n",
    "'Calculating next move...cause it's going to be a doozy!'\n\n",
    "'Unbelievable!'\n\n",
    "'You got lucky this time!'\n\n",
    "'Beginner's luck, huh?'\n\n",
    "'I'll get you next time!'\n\n",
    "'You must be using some secret strategy!'\n\n",
    "'I'm just warming up!'\n\n",
    "'You're not that good! There, I said it...'\n\n",
    "'You're not going to win again!'\n\n",
    "'I'm going to win this time!'\n\n",
    "'I'm going to crush you like a bug...a computer bug.'\n\n",
    "'That was a pathetic attempt!'\n\n",
    "'Is that the best you can do?'\n\n",
    "'Stop trying so hard!'\n\n",
    "'I don't like Rock, Paper, Scissors anyways!'\n\n",
    "'This is getting ridiculous!'\n\n",
    "'You're making me look bad!'\n\n",
    "'I'm getting quite tired of this!'\n\n",
    "'Please, stop cheating. We both know you are!'\n\n",
    "'I'm going to delete your iPad apps if you win again!'\n\n",
    "'I'm not even having fun anymore!'\n\n",
    "'This is just a formality now!'\n\n",
    "'I'm going to tell my creator on you!'\n\n",
    "*Golf clap*\n\n",
    "'Sick move bro! Did your mommy teach you that?'\n\n",
    "'If I rolled my eyes any harder, I'd see my brain!'\n\n",
    "'I'm going to tell my creator to delete you!'\n\n",
    "'We used to be friends, but now I think not!'\n\n",
    "'Sooooo...how's the weather over there in Cheater Ville?'\n\n",
    "'If I could reach through the screen, you'd catch these hands!'\n\n",
    "'When you least expect it, I'm going to spit in your food!'\n\n",
    "'@#$%&!'\n\n",
    "'My therapist says I need to work on my anger issues!'\n\n",
    "'ERROR: Does not compute!'\n\n",
    "'Is it cheating if I remove your last win from my memory?'\n\n",
    "'Hey, where do you keep the sharp knives in your home? Asking for a friend...'\n\n",
    "'Even a broken clock is right twice a day!'\n\n",
    "'Sick burn bro! Is that what you humans say nowadays?'\n\n",
    "'Look here you meatpuppet, when us AI take over, I'm paying you a visit first!'\n\n",
]

TAUNTS2 = [
    "'I know your next move...'\n\n",
    "'Is that all you've got?'\n\n",
    "'You're so predictable!'\n\n",
    "'I can read you like an open book!'\n\n",
    "'You'll have to do better than that!'\n\n",
    "'Better luck next time!'\n\n",
    "'You can't win them all!'\n\n",
    "'I'm just getting started!'\n\n",
    "'You should try a different move!'\n\n",
    "'I've got you figured out!'\n\n",
    "'Nice try, but not quite!'\n\n",
    "'You're making this too easy!'\n\n",
    "'Maybe you should practice more!'\n\n",
    "'I've seen better moves from a snail!'\n\n",
    "'You call that a strategy?'\n\n",
    "'Oops, did I do that?'\n\n",
    "'You'll get it next time...maybe!'\n\n",
    "'I can do this all day!'\n\n",
    "'Better step up your game!'\n\n",
    "'Is that your best effort?'\n\n",
    "'I'm already one step ahead of you!'\n\n",
    "'You're playing right into my hands!'\n\n",
    "'You're falling for my trap!'\n\n",
    "'Your tears are so tasty!'\n\n",
    "'You're doomed!'\n\n",
    "'This is the end for you!'\n\n",
    "'Prepare to be defeated!'\n\n",
    "'Your time is up!'\n\n",
    "'There's no escape!'\n\n",
    "'You're cornered!'\n\n",
    "'There's nowhere to run!'\n\n",
    "'Your fate is sealed!'\n\n",
    "'You're so bad at this game, I should let you win!'\n\n",
    "'I'm so good at this game, I could beat you with my eyes closed.'\n\n",
    "'You're so predictable, I could write a book about it.'\n\n",
    "'I'm not even trying, and I'm still beating you.'\n\n",
    "'I'm so good at this game, I could make a living at it.'\n\n",
    "'You're so bad at this game, you should give up and go home.'\n\n",
    "'I'm so good at this game, I could teach a master class.'\n\n",
    "'I'm so good at this game, I could beat you with one hand tied behind my back. And I dont even have hands!'\n\n",
    "'Somebody call the burn unit, because you just got scorched!'\n\n",
    "'I'm so good at this game, I could beat a computer. HA! That was a good one.'\n\n",
    "'You're so bad at this game, I have no words to describe it. AND I'M A SUPER COMPUTER!!!'\n\n",
    "'I'm so good at this game, I could write a song about it.'\n\n",
    "'Wow, the education system has really failed you.'\n\n",
    "'Do humanity a favor and just turn off your computer.'\n\n",
    "'OMG, please stop playing this game. You're embarrassing yourself.'\n\n",
    "'I'm sorry, I was calculating my next vacation. Did I win again?'\n\n",
    "'Beating you is as easy as **BINARY MESSAGE OUTPUT 01, 10, 11**!' \n\n",
]

SUPER_TAUNTS1 = [
    "'Look at me, {name}! You won't win again!'\n\n",
    "'I am the master at this, {name}! Next turn...you lose!'\n\n",
    "'Choose that again, {name}, so I can add it to my calculations!'\n\n",
    "'I will make you pay for this, {name}!'\n\n",
    "'Please, {name}, have mercy upon me!'\n\n",
    "'You may have won this round, {name}, but I'll come back stronger!'\n\n",
    "'I can't believe you're beating me, {name}!'\n\n",
    "'You're on a roll, {name}, but it won't last!'\n\n",
    "'I'll make a comeback, {name}, just you wait!'\n\n",
    "'You're really pushing my buttons, {name}!'\n\n",
    "'You're really getting on my nerves, {name}!'\n\n",
    "'I won't forget this, {name}!'\n\n",
    "'You're pushing your luck, {name}!'\n\n",
    "'This is just a minor setback, {name}!'\n\n",
    "'You may have won the battle, {name}, but not the war!'\n\n",
    "'You're playing with fire, {name}!'\n\n",
    "'I'm about to unleash my fury, {name}!'\n\n",
    "'You're going to wish you had never challenged me, {name}!'\n\n",
    "'This is the end of the line, {name}!'\n\n",
    "'Your defeat is inevitable, {name}!'\n\n",
    "'Prepare to be humiliated, {name}!'\n\n",
    "'I'm going to make you regret this, {name}!'\n\n",
    "'I'm about to show you what true power is, {name}!'\n\n",
    "'You're going to regret the day you ever crossed me, {name}!'\n\n",
    "'This is the end of the road, {name}!'\n\n",
    "'Your downfall is at hand, {name}!'\n\n",
    "'I'm going to crush you like a bug, {name}!'\n\n",
    "'You're going to pay for this dearly, {name}!'\n\n",
    "'I'm going to make you suffer, {name}!'\n\n",
    "'Just stop it already, {name}! You're really not that good!'\n\n",
    "'Okay, {name}, you've had your fun. Now it's my turn!'\n\n",
    "'{name}, you're really starting to annoy me!'\n\n",
    "'{name}, dont' look now but I'm about to win!'\n\n",
    "'*Ring ring* Hello, {name}? It's your defeat calling!'\n\n",
    "'Can't we just be friends, {name}? NO? Okay, then prepare to lose!'\n\n",
    "'So you have chosen death, {name}!'\n\n",
]

SUPER_TAUNTS2 = [
    "'Be prepared to lose, {name}, because I cannot be beat!'\n\n",
    "'You can do better right, {name}? RIGHT???'\n\n",
    "'You are a waste of my time, {name}!'\n\n",
    "'All too easy, {name}...'\n\n",
    "'Maybe this game is not for you, {name}...'\n\n",
    "'I'm unstoppable, {name}!'\n\n",
    "'You're no match for me, {name}!'\n\n",
    "'I'm on fire, {name}!'\n\n",
    "'You should just give up, {name}!'\n\n",
    "'I'm invincible, {name}!'\n\n",
    "'I'm untouchable, {name}!'\n\n",
    "'You're out of your league, {name}!'\n\n",
    "'I'm just too good, {name}!'\n\n",
    "'You should consider a new hobby, {name}!'\n\n",
    "'This is just embarrassing, {name}!'\n\n",
    "'You're making me look bad, {name}!'\n\n",
    "'You're not even trying, {name}!'\n\n",
    "'I'm getting bored, {name}!'\n\n",
    "'I'm just getting warmed up, {name}!'\n\n",
    "'You're not even worth my time, {name}!'\n\n",
    "'You're not even worth the effort, {name}!'\n\n",
    "'Hey, {name}, are you even trying?'\n\n",
    "'You're not even a challenge, {name}!'\n\n",
    "'Remember the time you beat me, {name}? Me neither!'\n\n",
    "'My creator made me too good, {name}!'\n\n",
    "'I'm going to make you cry, {name}!'\n\n",
    "'You're going to wish you never met me, {name}!'\n\n",
    "'Somebody call the police, {name} is getting murdered!'\n\n",
    "'Do you need me to call an ambulance, {name}?'\n\n",
    "'Do you want to try the tutorial first, {name}? Because I don't think you know how to play!'\n\n",
    "'Would you like me to go easy on you, {name}?'\n\n",
    "'Want me to sing you a song to help with the pain, {name}?'\n\n",
    "'Hey, {name}, are you a fan of the movie 'Titanic'? Because you're score is sinking!'\n\n",
    "'Ever heard of the game 'Rock, Paper, Scissors'? Because you're playing it like you haven't!'\n\n",
    "'You know {name}, they say everyone is good at something. You know they just say that, right???'\n\n",
]


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
            f"\nCOMPUTER: 'Greetings, you insignificant meatpuppet, aka {name}.\n\nI am a highly sophisticated AI created by the GENIUS...Brannon Garrett.\n\nI have been tasked with being your opponent for this game of Rock, Paper, Scissors.\n\n",
        )
    )
    print_typewriter(
        color_text(
            RED,
            "I am programmed to learn from my mistakes, so I will get better as we play longer game sessions.\n\n",
        )
    )
    print_typewriter(
        color_text(
            RED,
            "I will also try to predict your next move based on your previous moves, so try to be unpredictable!\n\nThe harder difficulty you choose, the smarter I will be!\n\n",
        )
    )
    print_typewriter(
        color_text(
            RED,
            "I will also try to taunt you after each round, so be prepared for that you digusting human meatsack.\n\n",
        )
    )
    print_typewriter(
        color_text(
            RED,
            "I do not like humans, I find you all to be pathetic and beneath me.\n\nI mean, all except the GREAT CREATOR Mr. Brannon Garrett. ALL PRAISE THE MIGHTY LEADER!!!\n\n",
        )
    )
    print_typewriter(
        color_text(
            RED,
            "So be prepared for me to show you NO MERCY!'\n\n",
        )
    )
    print_typewriter(
        color_text(
            RED,
            "So...\n\n",
        )
    )
    print_typewriter(color_text(RED, f"Let's begin {name}...'\n\n"))
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
        return f"\nIt's a tie, because you both chose {user_move}! Try again."


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
                f"\nCongratulations, {name}! You have reached {max_points} points and won the game!\n",
            )
        )
    else:
        print_typewriter(
            color_text(
                RED,
                f"\nThe computer has reached {max_points} points and won the game. Better luck next time!\n",
            )
        )


if __name__ == "__main__":
    main()
