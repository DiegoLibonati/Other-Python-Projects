from random import random

intents = 0

try:
    number_range = int(input("Select a number range [If you select 10, the IA will select a random number from 0 to 10]: "))

    random_number = round(random() * number_range)

    print("¡Random number was generated, try to find the number!")

    user_find = int(input("Select a number: "))
except (ValueError, NameError):
    print("ERROR: You need to select a int number. Strings were not allowed")

while user_find != random_number:
    user_find = int(input("Oops, you fail but you can try again. Select a number: "))
    intents+=1

print(f"You won, the secret number was: {random_number} in {intents} times")