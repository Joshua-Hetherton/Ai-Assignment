import tkinter as tk

# Function to start the game
def start_game():
    root.withdraw()
    create_game_window()

# Function to quit the game
def quit_game():
    root.destroy()

# Function to create the game window
def create_game_window():
    game_window = tk.Toplevel(root)
    game_window.title("Tic-Tac-Toe")
    game_window.geometry("600x500")
    game_window.configure(bg="#2c3e50")  # Set background color

    # Initialize the game board
    global board, current_player, status_label, buttons
    board = [" " for _ in range(9)]
    current_player = "X"

    # Create a label to display the game status
    status_label = tk.Label(game_window, text="Player X's turn", font=('normal', 20), bg="#2c3e50", fg="#ecf0f1")
    status_label.pack(pady=10)

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
            buttons[index].config(text=current_player, fg="#2c3e50")
            if check_win():
                status_label.config(text=f"Player {current_player} wins!")
                disable_buttons()
            elif check_draw():
                status_label.config(text="It's a draw!")
                disable_buttons()
            else:
                current_player = "O" if current_player == "X" else "X"
                status_label.config(text=f"Player {current_player}'s turn")

    # Function to disable all buttons
    def disable_buttons():
        for button in buttons:
            button.config(state=tk.DISABLED)

    # Function to reset the game
    def reset_game():
        global board, current_player
        board = [" " for _ in range(9)]
        current_player = "X"
        for button in buttons:
            button.config(text=" ", state=tk.NORMAL)
        status_label.config(text="Player X's turn")
        show_reset_button()

    # Function to confirm reset
    def confirm_reset():
        reset_button.pack_forget()
        confirm_label.pack(pady=10)
        yes_button.pack(side=tk.LEFT, padx=10)
        no_button.pack(side=tk.RIGHT, padx=10)

    # Function to show reset button
    def show_reset_button():
        confirm_label.pack_forget()
        yes_button.pack_forget()
        no_button.pack_forget()
        reset_button.pack(pady=20)

    # Create buttons for the game board
    buttons = []
    button_frame = tk.Frame(game_window, bg="#2c3e50")
    button_frame.pack(pady=10)
    for i in range(9):
        button = tk.Button(button_frame, text=" ", font=('normal', 20), width=4, height=2, bg="#ecf0f1", command=lambda i=i: button_click(i))
        button.grid(row=i//3, column=i%3, padx=5, pady=5)
        buttons.append(button)

    # Create a reset button
    reset_button = tk.Button(game_window, text="Reset", font=('normal', 20), bg="#e74c3c", fg="#ecf0f1", command=confirm_reset)
    reset_button.pack(pady=20)

    # Create confirmation widgets
    confirm_label = tk.Label(game_window, text="Are you sure you want to reset the game?", font=('normal', 14), bg="#2c3e50", fg="#ecf0f1")
    yes_button = tk.Button(game_window, text="Yes", font=('normal', 14), bg="#27ae60", fg="#ecf0f1", command=reset_game)
    no_button = tk.Button(game_window, text="No", font=('normal', 14), bg="#c0392b", fg="#ecf0f1", command=show_reset_button)

    # Ensure the root window is destroyed when the game window is closed
    game_window.protocol("WM_DELETE_WINDOW", quit_game)

    # Run the Tkinter event loop
    game_window.mainloop()

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x500")
root.configure(bg="#2c3e50")  # Set background color

# Create the title screen
title_screen = tk.Frame(root, bg="#2c3e50")
title_screen.pack(pady=50)

title_label = tk.Label(title_screen, text="Tic-Tac-Toe", font=('normal', 40), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

start_button = tk.Button(title_screen, text="Start", font=('normal', 20), bg="#27ae60", fg="#ecf0f1", command=start_game)
start_button.pack(pady=10)

quit_button = tk.Button(title_screen, text="Quit", font=('normal', 20), bg="#c0392b", fg="#ecf0f1", command=quit_game)
quit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()