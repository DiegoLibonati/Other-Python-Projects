from random import choice
from time import sleep

grid_board = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]
game_finish = False
count = 0

def generate_board_game(grid_board):

    for grid in grid_board:
        print(grid)

    return 

def change_grid(grid_board, user_value_grid, symbol, possible_choices):

    global count

    for line in grid_board:
        for index, element in enumerate(line):
            if user_value_grid == element:
                line[index] = symbol
                count += 1
                possible_choices.pop(possible_choices.index(user_value_grid))
                return generate_board_game(grid_board), line[index]

    user_value_grid = input("Oops, select other: ")
    return change_grid(grid_board, user_value_grid, symbol, possible_choices)

def check_game_finish(symbolA, symbolB):
    
    global game_finish

    if symbolA == grid_board[0][0] and symbolA == grid_board[0][1] and symbolA == grid_board[0][2] or \
        symbolA == grid_board[1][0] and symbolA == grid_board[1][1] and symbolA == grid_board[1][2] or \
        symbolA == grid_board[2][0] and symbolA == grid_board[2][1] and symbolA == grid_board[2][2] or \
        symbolA == grid_board[0][0] and symbolA == grid_board[1][0] and symbolA == grid_board[2][0] or \
        symbolA == grid_board[0][1] and symbolA == grid_board[1][1] and symbolA == grid_board[2][1] or \
        symbolA == grid_board[0][2] and symbolA == grid_board[1][2] and symbolA == grid_board[2][2] or \
        symbolA == grid_board[0][0] and symbolA == grid_board[1][1] and symbolA == grid_board[2][2] or \
        symbolA == grid_board[0][2] and symbolA == grid_board[1][1] and symbolA == grid_board[2][0]:
        game_finish = True
        return print("PLAYER A WINS!")

    elif symbolB == grid_board[0][0] and symbolB == grid_board[0][1] and symbolB == grid_board[0][2] or \
        symbolB == grid_board[1][0] and symbolB == grid_board[1][1] and symbolB == grid_board[1][2] or \
        symbolB == grid_board[2][0] and symbolB == grid_board[2][1] and symbolB == grid_board[2][2] or \
        symbolB == grid_board[0][0] and symbolB == grid_board[1][0] and symbolB == grid_board[2][0] or \
        symbolB == grid_board[0][1] and symbolB == grid_board[1][1] and symbolB == grid_board[2][1] or \
        symbolB == grid_board[0][2] and symbolB == grid_board[1][2] and symbolB == grid_board[2][2] or \
        symbolB == grid_board[0][0] and symbolB == grid_board[1][1] and symbolB == grid_board[2][2] or \
        symbolB == grid_board[0][2] and symbolB == grid_board[1][1] and symbolB == grid_board[2][0]:
        game_finish = True
        return print("PLAYER B WINS!")

    elif count == 9:
        game_finish = True
        return print("TIED GAME!")

def user_vs_user():

    possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    userA_symbol = input("[USER A] Select your symbol like [X or O] but you can select other: ")
    userB_symbol = input("[USER B] Select your symbol like [X or O] but you can select other: ")

    while userB_symbol == userA_symbol:
        userB_symbol = input("[USER B] Select your symbol like [X or O] but you can select other: ")

    while game_finish == False:
        userA = input("User A plays: ").upper()
        change_grid(grid_board, userA, userA_symbol, possible_choices)
        check_game_finish(userA_symbol, userB_symbol)

        if game_finish:
            break

        userB = input("User B plays: ").upper()
        change_grid(grid_board, userB, userB_symbol, possible_choices)
        check_game_finish(userA_symbol, userB_symbol)

def user_vs_IA():

    possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    IA_symbol = "X"
    user_symbol = input("[USER] Select your symbol like [X or O] but you can select other: ")

    while user_symbol == IA_symbol:
        user_symbol = input("[USER] Select your symbol like [X or O] but you can select other: ")

    while game_finish == False:
        user = input("User plays: ").upper()
        change_grid(grid_board, user, user_symbol, possible_choices)
        check_game_finish(user_symbol, IA_symbol)
        sleep(1)
        if game_finish:
            break
        
        IA_plays = choice(possible_choices)
        print(f"IA plays: {IA_plays}")
        change_grid(grid_board, IA_plays, IA_symbol, possible_choices)
        check_game_finish(user_symbol, IA_symbol)

def IA_vs_IA():

    possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    IA_one_symbol = "X"
    IA_two_symbol = "O"

    while game_finish == False:
        IA_one_plays = choice(possible_choices)
        print(f"IA One plays: {IA_one_plays}")
        change_grid(grid_board, IA_one_plays, IA_one_symbol, possible_choices)
        check_game_finish(IA_one_symbol,IA_two_symbol)
        sleep(1)

        if game_finish:
            break
        
        IA_two_plays = choice(possible_choices)
        print(f"IA Two plays: {IA_two_plays}")
        change_grid(grid_board, IA_two_plays, IA_two_symbol, possible_choices)
        check_game_finish(IA_one_symbol,IA_two_symbol)
        sleep(1)

print("Select MODE:\n 1) User VS User\n 2) User vs IA\n 3) IA vs IA\n")

try:
    mode_selected = int(input("Select a number of MODE: "))

    while mode_selected < 1 or mode_selected > 3:
        mode_selected = int(input("Select a number of MODE: "))

    if mode_selected == 1:
        user_vs_user()
    elif mode_selected == 2:
        user_vs_IA()
    elif mode_selected == 3:
        IA_vs_IA()
except ValueError:
    print("That´s not an int!")