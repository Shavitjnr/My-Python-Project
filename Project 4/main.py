#   The Perfect Guess
import random
n = random.randint(1, 100)
a = 1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a number: "))
    if(a >n):
        print("Low Number PLease")
    else:
        print("Higher NUmber PLease")

print(f"You have guesses the number correctly in {guesses} attempts.")