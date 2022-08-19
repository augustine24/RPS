import random
# random has to be imported in order for the random generator from the computer's end has to be implemented.
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    # This implements the question to the user, asking them to choose something between rock, paper and scissors.
    # The user should only select out of these 3 options for the input.
    possible_actions = ["rock", "paper", "scissors"]
    # These are the possible results 
    computer_action = random.choice(possible_actions)
    # The random.choice syntax is only usable because random was imported. The possible results are all randomized, but not from the user.
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    # The above code starting from if, shows the conditions that are shown to the user, as well as programs what happens depending on 
    # what the randomized response is to the user picking rock, paper or scissors.

    play_again = input("Play again? (y/n): ")
    # This code is to give the user a chance to play again, an input is required from the user to confirm if they would like to, using y or n.
    if play_again.lower() != "y":
        break
