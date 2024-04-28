# Ayu Jannati Ali Putri
# 122140201
# Tugas Praktikum PBO

import tkinter as tk
from tkinter import messagebox
import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class HumanPlayer(Player):
    def move(self):
        pass

class ComputerPlayer(Player):
    def move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == 0]
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return None

# Fungsi untuk menampilkan pesan pemenang
def show_winner(winner):
    if winner == 0:
        messagebox.showinfo("Game Over", "It's a Draw!")
    else:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")

# Fungsi untuk mengecek kemenangan
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]

    if all([all(row) for row in board]):
        return 0

    return None

# Fungsi untuk mengatur tampilan tombol setelah diklik
def button_click(row, col):
    global current_player, winner, board
    if board[row][col] == 0 and not winner:
        buttons[row][col].config(text=current_player.symbol, state=tk.DISABLED)
        board[row][col] = current_player.symbol
        winner_check = check_winner(board)
        if winner_check:
            show_winner(winner_check)
            winner = winner_check
        current_player = player1 if current_player == player2 else player2
        if isinstance(current_player, ComputerPlayer):
            move = current_player.move()
            if move:
                row, col = move
                button_click(row, col)

# Fungsi untuk mereset permainan
def reset_game():
    global winner, board, current_player
    winner = None
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state=tk.NORMAL)
    current_player = player1

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Tic Tac Toe")

# Variabel global
player1 = HumanPlayer("X")
player2 = ComputerPlayer("O")
current_player = player1  
winner = None  
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  

# Membuat tombol-tombol permainan
buttons = [[None, None, None], [None, None, None], [None, None, None]]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Helvetica", 20), width=6, height=2,
                                      command=lambda row=row, col=col: button_click(row, col))
        buttons[row][col].grid(row=row, column=col, sticky="nsew")

# Tombol reset
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Mengatur ukuran jendela
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure