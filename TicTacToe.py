board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

ongoing_game = True

winner = None

current_player = "X"

def display_the_board():
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print("-------------")

def play_the_game():
    display_the_board()

    while ongoing_game:
        handle_turn(current_player)
        check_status()
        change_player()
    if winner == "X" or winner == "O":
        print(f"Player {winner} Won")
    elif winner == None:
        print("It's a tie")
          
def handle_turn(player):

    print(f"Turn for Player {player}")
    position = input("Choose a position from 1 to 9: ")
    valid = False 
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9",]:
            position = input("Try numbers from 1 to 9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("This position is already filled!")

    board[position] = player
    display_the_board() 

def check_status():
    check_win()
    check_tie()  

def check_win():

    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global ongoing_game
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        ongoing_game = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]    
    return

def check_columns():
    global ongoing_game
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        ongoing_game = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2] 
    return

def check_diagonals():
    global ongoing_game
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        ongoing_game = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return

def check_tie():
    global ongoing_game
    if "-" not in board:
        ongoing_game = False
    return

def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_the_game()    

     