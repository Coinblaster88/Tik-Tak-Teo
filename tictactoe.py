#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
- Play against AI (with minimax algorithm)
- Play against a friend (2-player mode)
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        
        # Game state
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_mode = None  # 'ai' or '2player'
        self.game_active = False
        
        # Create UI
        self.create_mode_selection()
        
    def create_mode_selection(self):
        """Create mode selection screen"""
        self.mode_frame = tk.Frame(self.root, padx=20, pady=20)
        self.mode_frame.pack()
        
        title = tk.Label(
            self.mode_frame,
            text="Tic-Tac-Toe",
            font=('Arial', 24, 'bold')
        )
        title.pack(pady=10)
        
        subtitle = tk.Label(
            self.mode_frame,
            text="Choose Game Mode",
            font=('Arial', 14)
        )
        subtitle.pack(pady=5)
        
        ai_button = tk.Button(
            self.mode_frame,
            text="Play vs AI",
            font=('Arial', 14),
            width=20,
            height=2,
            command=lambda: self.start_game('ai')
        )
        ai_button.pack(pady=10)
        
        two_player_button = tk.Button(
            self.mode_frame,
            text="2 Player Mode",
            font=('Arial', 14),
            width=20,
            height=2,
            command=lambda: self.start_game('2player')
        )
        two_player_button.pack(pady=10)
        
    def start_game(self, mode):
        """Start game with selected mode"""
        self.game_mode = mode
        self.game_active = True
        self.mode_frame.destroy()
        self.create_game_board()
        
    def create_game_board(self):
        """Create the game board UI"""
        # Top frame with info and reset button
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)
        
        mode_text = "vs AI" if self.game_mode == 'ai' else "2 Player"
        self.mode_label = tk.Label(
            top_frame,
            text=f"Mode: {mode_text}",
            font=('Arial', 12)
        )
        self.mode_label.pack(side=tk.LEFT, padx=10)
        
        self.status_label = tk.Label(
            top_frame,
            text="Player X's Turn",
            font=('Arial', 12, 'bold')
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        reset_button = tk.Button(
            top_frame,
            text="Reset",
            font=('Arial', 10),
            command=self.reset_game
        )
        reset_button.pack(side=tk.LEFT, padx=10)
        
        menu_button = tk.Button(
            top_frame,
            text="Main Menu",
            font=('Arial', 10),
            command=self.back_to_menu
        )
        menu_button.pack(side=tk.LEFT, padx=10)
        
        # Game board frame
        board_frame = tk.Frame(self.root)
        board_frame.pack(pady=10)
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text='',
                    font=('Arial', 32, 'bold'),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                self.buttons[i][j] = button
                
    def make_move(self, row, col):
        """Handle player move"""
        if not self.game_active or self.board[row][col] != '':
            return
            
        # Make the move
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(
            text=self.current_player,
            state='disabled',
            disabledforeground='blue' if self.current_player == 'X' else 'red'
        )
        
        # Check for win or draw
        if self.check_winner(self.board, self.current_player):
            self.game_active = False
            winner_text = "You win!" if self.game_mode == 'ai' else f"Player {self.current_player} wins!"
            messagebox.showinfo("Game Over", winner_text)
            self.status_label.config(text=f"{winner_text}")
            return
            
        if self.is_board_full(self.board):
            self.game_active = False
            messagebox.showinfo("Game Over", "It's a draw!")
            self.status_label.config(text="It's a draw!")
            return
            
        # Switch player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Player {self.current_player}'s Turn")
        
        # AI's turn if in AI mode and current player is O
        if self.game_mode == 'ai' and self.current_player == 'O':
            self.root.after(500, self.ai_move)
            
    def ai_move(self):
        """AI makes a move using minimax algorithm"""
        if not self.game_active:
            return
            
        self.status_label.config(text="AI is thinking...")
        self.root.update()
        
        best_score = float('-inf')
        best_move = None
        
        # Try all possible moves
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    # Try this move
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ''
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        # Make the best move
        if best_move:
            row, col = best_move
            self.make_move(row, col)
            
    def minimax(self, board, depth, is_maximizing):
        """Minimax algorithm for AI"""
        # Check terminal states
        if self.check_winner(board, 'O'):
            return 10 - depth
        if self.check_winner(board, 'X'):
            return depth - 10
        if self.is_board_full(board):
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score
            
    def check_winner(self, board, player):
        """Check if player has won"""
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
        
    def is_board_full(self, board):
        """Check if board is full"""
        return all(board[i][j] != '' for i in range(3) for j in range(3))
        
    def reset_game(self):
        """Reset the game board"""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_active = True
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text='',
                    state='normal'
                )
                
        self.status_label.config(text="Player X's Turn")
        
    def back_to_menu(self):
        """Return to main menu"""
        # Destroy current widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Reset game state
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_mode = None
        self.game_active = False
        
        # Show mode selection
        self.create_mode_selection()

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
