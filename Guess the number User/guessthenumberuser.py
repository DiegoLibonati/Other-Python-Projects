from random import random
from time import sleep

numbers_chosen = []

number_selected = int(input("Select a random number: "))

number_selected_ia = round(random() * number_selected)
numbers_chosen.append(number_selected_ia)
print(f"The IA choose: {number_selected_ia}")

def check_repeat_number_chosen(n):
    if n not in numbers_chosen:
        numbers_chosen.append(number_selected_ia)
        sleep(1)
        return print(f"Oops, the computers fail. Try again bot. The IA choose: {number_selected_ia}")
    else:
        pass

sleep(1)

while number_selected != number_selected_ia:

    number_selected_ia = round(random() * number_selected)
    check_repeat_number_chosen(number_selected_ia)
    

print("The computer finally found the secret number.")
