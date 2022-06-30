grid_board = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]
game_finish = False
count = 0

def generate_board_game(grid_board):

    for grid in grid_board:
        print(grid)

    return 

def select_who_plays():
    print("Select MODE:\n 1) User VS User\n 2) User vs IA\n 3) IA vs IA\n")

    mode_selected = int(input("Select a number of MODE: "))

    if mode_selected == 1:
        user_vs_user()

def change_grid(grid_board, user_value_grid, symbol):

    global count

    for line in grid_board:
        for index, element in enumerate(line):
            if user_value_grid == element:
                line[index] = symbol
                count += 1
                return generate_board_game(grid_board)

    user_value_grid = input("Oops, select other: ")
    return change_grid(grid_board, user_value_grid, symbol)

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
        return print("USER A WINS!")

    elif symbolB == grid_board[0][0] and symbolB == grid_board[0][1] and symbolB == grid_board[0][2] or \
        symbolB == grid_board[1][0] and symbolB == grid_board[1][1] and symbolB == grid_board[1][2] or \
        symbolB == grid_board[2][0] and symbolB == grid_board[2][1] and symbolB == grid_board[2][2] or \
        symbolB == grid_board[0][0] and symbolB == grid_board[1][0] and symbolB == grid_board[2][0] or \
        symbolB == grid_board[0][1] and symbolB == grid_board[1][1] and symbolB == grid_board[2][1] or \
        symbolB == grid_board[0][2] and symbolB == grid_board[1][2] and symbolB == grid_board[2][2] or \
        symbolB == grid_board[0][0] and symbolB == grid_board[1][1] and symbolB == grid_board[2][2] or \
        symbolB == grid_board[0][2] and symbolB == grid_board[1][1] and symbolB == grid_board[2][0]:
        game_finish = True
        return print("USER B WINS!")

    elif count == 9:
        game_finish = True
        return print("TIED GAME!")

def user_vs_user():

    userA_symbol = input("[USER A] Select your symbol like [X or O] but you can select other: ")
    userB_symbol = input("[USER B] Select your symbol like [X or O] but you can select other: ")

    while userB_symbol == userA_symbol:
        userB_symbol = input("[USER B] Select your symbol like [X or O] but you can select other: ")

    while game_finish == False:
        userA = input("User A plays: ").upper()
        change_grid(grid_board, userA, userA_symbol)
        check_game_finish(userA_symbol, userB_symbol)

        if game_finish:
            break

        userB = input("User B plays: ").upper()
        change_grid(grid_board, userB, userB_symbol)
        check_game_finish(userA_symbol, userB_symbol)

        
select_who_plays()