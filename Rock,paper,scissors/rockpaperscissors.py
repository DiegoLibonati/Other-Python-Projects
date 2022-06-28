from random import randint

ia_choose = ["rock", "paper", "scissors"]
round = 1
user_score = 0
ia_score = 0

def generate_random_number():
    return randint(0, len(ia_choose)-1)

def check_result_of_round(ia, user):

    global user_score
    global ia_score

    if ia == "rock" and user == 0 or ia == "paper" and user == 1 or ia =="scissors" and user == 2:
        return print(f"Tied round: IA: {ia} | User: {ia_choose[user]}")
    elif ia == "rock" and user == 1 or ia =="paper" and user == 2 or ia == "scissors" and user == 0:
        user_score += 1
        return print(f"User won the round: IA: {ia} | User: {ia_choose[user]}")
    elif ia =="rock" and user == 2 or ia == "paper" and user == 0 or ia == "scissors" and user == 1:
        ia_score += 1
        return print(f"IA won the round: IA: {ia} | User: {ia_choose[user]}")

def check_final_result_scores():
    if user_score > ia_score:
        return print("¡USER WIN!")
    elif ia_score > user_score:
        return print("¡IA WIN!")
    elif ia_score == user_score:
        return print("¡ITS A TIED GAME!")


while round <= 3:
    print(f"Ronda {round}")
    ia_chosen = ia_choose[generate_random_number()]
    user_chosen = int(input("Choose a number: 0. Rock / 1. Paper / 2. Scissors: "))

    if user_chosen < 0 or user_chosen > 2 or type(user_chosen) != int:
        raise Exception("Insert a correct value.")

    check_result_of_round(ia_chosen, user_chosen)
    round += 1

check_final_result_scores()