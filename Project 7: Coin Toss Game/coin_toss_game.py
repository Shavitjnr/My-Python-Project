#  Coin Toss Game
import random

def get_computer_choice():
    choices = ["Heads", "Tails"]
    return random.choice(choices)


def get_user_choice():
    user_input = input("Enter Heads or Tails: ").capitalize()
    while user_input not in ["Heads", "Tails"]:
        print("Invalid choice. Try again.")
        user_input = input("Enter Heads or Tails: ").capitalize()
    return user_input

print("Welcome to the Coin Toss Game!")

computer_choice = get_computer_choice()
user_choice = get_user_choice()

print(f"Computer chose: {computer_choice}")
print(f"You chose: {user_choice}")

if computer_choice == user_choice:
    print("It's a tie!")
elif (computer_choice == "Heads" and user_choice == "Tails") or (computer_choice == "Tails" and user_choice == "Heads"):
    print("You win!")
else:
    print("Computer wins!")
    
