from random import randint
from time import sleep

numbers_chosen = []

ranged_selected = int(input("Select a max ranged: "))
random_number = int(input(f"Select a random number in range: {ranged_selected}: "))

while random_number > ranged_selected or random_number < 0:
    random_number = int(input(f"Select a random number in range: {ranged_selected}: "))

ia_number_selected = randint(0, ranged_selected)
numbers_chosen.append(ia_number_selected)
print(f"The computer plays: {ia_number_selected}")
sleep(1)

while ia_number_selected != random_number:
    ia_number_selected = randint(0, ranged_selected)
    if ia_number_selected not in numbers_chosen:
        numbers_chosen.append(ia_number_selected)
        print(f"Oops, you fail. Try again bot. The computer plays: {ia_number_selected}")
        sleep(1)
    else:
        pass

print("The computer finally find the secret number.")