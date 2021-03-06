# Python Source Code for Tic Tac Toe by @bskumawat09
# 06-Mar-2021

# global variables
game_is_running = True

# initially there is no winner
winner = None

# X will play a first turn
current_player = "X"

# tic tac toe board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# starting point of game
def play_game():
    global winner

    # display initial board
    display_board()

    # while the game is running
    while game_is_running:
        # handles the turn for current player
        handle_turn(current_player)

        # check if game has ended
        is_game_over()

        # flip the turn
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print("Congratulations! " + winner + " won")

    elif winner is None:
        print("Oops! Game tied")


def is_game_over():
    # check if one of the player won
    check_for_winner()

    # check if game is tied
    check_tie()


def check_for_winner():
    global winner

    # check row
    row_winner = row_check()

    # check column
    col_winner = col_check()

    # check diagonal
    dig_winner = dig_check()

    # get the winner
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dig_winner:
        winner = dig_winner
    else:
        winner = None


def row_check():
    global game_is_running

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_running = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]


def col_check():
    global game_is_running

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_is_running = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]


def dig_check():
    global game_is_running

    dig_1 = board[0] == board[4] == board[8] != "-"
    dig_2 = board[2] == board[4] == board[6] != "-"

    if dig_1 or dig_2:
        game_is_running = False
    if dig_1:
        return board[0]
    if dig_2:
        return board[2]


def check_tie():
    global game_is_running

    if "-" not in board:
        game_is_running = False


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


def handle_turn(player):
    print(player + "\'s turn")
    position = int(input("choose a position 1-9: ")) - 1

    # while the input is invalid keeps on asking for correct input
    while invalid_position(position):
        position = int(input("Invalid input, choose a position 1-9: ")) - 1

    board[position] = player

    display_board()


def invalid_position(position):
    # if position is not in range(0, 9)
    if position not in range(0, 9):
        return True

    # if it tries to over-write already filled value
    if board[position] != "-":
        print("Position is already filled")
        return True

    return False


play_game()
