import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables to keep track of the board and the current player
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def is_winner(board, player):
    """Check if a player has won"""
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Check if the board is full"""
    return all(cell != " " for row in board for cell in row)

def on_button_click(row, col):
    global current_player
    if board[row][col] == " ":
        # Update the board and button text
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        # Check for a winner
        if is_winner(board, current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif is_board_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This cell is already taken!")

def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")

# Set up the buttons in a grid
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                                      command=lambda r=row, c=col: on_button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Run the application
root.mainloop()