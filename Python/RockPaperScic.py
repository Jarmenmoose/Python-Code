#Rock Paper Scisscors Game
import random

keep_going = True
while keep_going:

    user_action = input("Choose your weapon (rock, paper, scissors): ")

    possible_actions  = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\nYour weapon {user_action}, Computer's weapon {computer_action}.\n")

    if user_action == computer_action:
        print(f"Tie")
    elif user_action =="Rock":
        if computer_action == "Scissors":
            print("Rock beats Scissors! You win.")
        else:
            print("Paper beats Rock! You lose")

    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper beats Rock! You win.")
        else:
            print("Scissors beat Paper! You lose")

    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissor beat Paper! You win.")
        else:
            print("Rock beats Scissor! You lose.")
    if user_action != ("Rock" or "Paper" or "Scissors"):
        keep_going = False
