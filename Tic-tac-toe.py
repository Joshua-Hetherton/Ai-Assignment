import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the game board
board = [" " for _ in range(9)]
current_player = "X"

# Function to check for a win
def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False

# Function to check for a draw
def check_draw():
    return " " not in board

# Function to handle button click
def button_click(index):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_win():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ")

# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Run the Tkinter event loop
root.mainloop()