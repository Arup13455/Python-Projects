'''def sum(a,b,c):
    return a + b + c

def printBoard(xstate,zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")

def check_win(xstate,zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3):
            print("X won the match!")
            return 1
        if(sum(zstate[win[0]],zstate[win[1]],zstate[win[2]]) == 3):
            print("O won the match!")
            return 0
    return -1
if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for X and 0 for O                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    print("Welcome to Tic tac toe!")
    while(True):
        printBoard(xstate,zstate)
        if(turn == 1):
           print("X's chance")
           value = int(input("Enter a value: "))
           xstate[value] = 1
        else:
           print("O's chance")
           value = int(input("Enter a value: "))
           zstate[value] = 1
        cwin = check_win(xstate,zstate)
        if(cwin != -1):
            break
        turn = 1 - turn
'''
'''# Tic Tac Toe
# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if there is a winner
def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True, board[i]
            
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True, board[i]
            
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True, board[0]
    if board[2] == board[4] == board[6] != ' ':
        return True, board[2]
    
    return False, None

# Function to play the game
def play_game():
    current_player = 'X' # Player X goes first
    
    while True:
        print_board()
        
        # Get the player's move
        while True:
            position = int(input(f"{current_player}, enter your move (1-9): ")) - 1
            if position >= 0 and position < 9 and board[position] == ' ':
                break
            else:
                print("Invalid move! Try again.")
        
        # Update the board
        board[position] = current_player
        
        # Check for a winner
        winner, symbol = check_winner()
        if winner:
            print_board()
            print(f"Player {symbol} wins!")
            break
        
        # Check for a tie
        if ' ' not in board:
            print_board()
            print("It's a tie!")

            # Ask the user if they want to restart
            restart = input("Do you want to play again? (yes/no): ")

            if restart.lower() == "yes":
                play_game()
            else:
                break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()'''

def print_board(board):
    """Print the Tic Tac Toe board"""
    for row in board:
        print("|".join(row))
        print("-+-+-")

def is_winner(board, player):
    """Check if a player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Check if the board is full"""
    return all(cell != " " for row in board for cell in row)

def play_game():
    """Start the Tic Tac Toe game"""
    board = [[" ", " ", " "] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"It's {current_player} turn")
        # Get user's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check if the current player has won
        if is_winner(board, current_player):
            print("Player", current_player, "wins!")
            break

        # Check if the game is a draw
        if is_board_full(board):
            print("It's a draw!")

            # Ask the user if they want to restart
            restart = input("Do you want to play again? (yes/no): ")

            if restart.lower() == "yes":
                play_game()
            else:
                break

        # Switch to the next player
        current_player = "O" if current_player == "X" else "X"

play_game()