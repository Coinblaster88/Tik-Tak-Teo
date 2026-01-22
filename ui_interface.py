"""
UI Module
Handles the graphical user interface using tkinter
"""

import tkinter as tk
from tkinter import messagebox
from game_logic import GameBoard
from ai_player import TicTacToeAI

class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)
        
        # Game components
        self.game_board = GameBoard()
        self.ai = TicTacToeAI()
        
        # Game state
        self.game_mode = None  # 'ai' or '2player'
        self.game_active = False
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Start with mode selection
        self.show_mode_selection()
        
    def show_mode_selection(self):
        """Display mode selection screen"""
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
            bg='#4CAF50',
            fg='white',
            command=lambda: self.start_game('ai')
        )
        ai_button.pack(pady=10)
        
        two_player_button = tk.Button(
            self.mode_frame,
            text="2 Player Mode",
            font=('Arial', 14),
            width=20,
            height=2,
            bg='#2196F3',
            fg='white',
            command=lambda: self.start_game('2player')
        )
        two_player_button.pack(pady=10)
        
    def start_game(self, mode):
        """Initialize game with selected mode"""
        self.game_mode = mode
        self.game_active = True
        self.game_board.reset()
        self.mode_frame.destroy()
        self.create_game_ui()
        
    def create_game_ui(self):
        """Create the game board interface"""
        # Top control panel
        top_frame = tk.Frame(self.root, bg='#f0f0f0')
        top_frame.pack(pady=10, fill=tk.X)
        
        mode_text = "vs AI" if self.game_mode == 'ai' else "2 Player"
        self.mode_label = tk.Label(
            top_frame,
            text=f"Mode: {mode_text}",
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        self.mode_label.pack(side=tk.LEFT, padx=10)
        
        self.status_label = tk.Label(
            top_frame,
            text="Player X's Turn",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#2196F3'
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        reset_button = tk.Button(
            top_frame,
            text="Reset",
            font=('Arial', 10),
            bg='#FF9800',
            fg='white',
            command=self.reset_game
        )
        reset_button.pack(side=tk.LEFT, padx=10)
        
        menu_button = tk.Button(
            top_frame,
            text="Main Menu",
            font=('Arial', 10),
            bg='#607D8B',
            fg='white',
            command=self.back_to_menu
        )
        menu_button.pack(side=tk.LEFT, padx=10)
        
        # Game board
        board_frame = tk.Frame(self.root, bg='#333333', padx=5, pady=5)
        board_frame.pack(pady=10)
        
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text='',
                    font=('Arial', 32, 'bold'),
                    width=5,
                    height=2,
                    bg='white',
                    command=lambda row=i, col=j: self.handle_click(row, col)
                )
                button.grid(row=i, column=j, padx=3, pady=3)
                self.buttons[i][j] = button
                
    def handle_click(self, row, col):
        """Handle player click on a cell"""
        if not self.game_active or not self.game_board.is_valid_move(row, col):
            return
            
        # Make the move
        current_player = self.game_board.current_player
        self.game_board.make_move(row, col, current_player)
        self.update_button(row, col, current_player)
        
        # Check game end conditions
        if self.check_game_end(current_player):
            return
            
        # Switch player
        self.game_board.switch_player()
        self.update_status()
        
        # AI's turn if in AI mode
        if self.game_mode == 'ai' and self.game_board.current_player == 'O':
            self.root.after(500, self.ai_make_move)
            
    def ai_make_move(self):
        """Let the AI make a move"""
        if not self.game_active:
            return
            
        self.status_label.config(text="AI is thinking...")
        self.root.update()
        
        # Get best move from AI
        move = self.ai.get_best_move(self.game_board)
        
        if move:
            row, col = move
            self.game_board.make_move(row, col, 'O')
            self.update_button(row, col, 'O')
            
            # Check game end
            if self.check_game_end('O'):
                return
                
            # Switch back to player
            self.game_board.switch_player()
            self.update_status()
            
    def update_button(self, row, col, player):
        """Update button appearance after move"""
        color = '#2196F3' if player == 'X' else '#F44336'
        self.buttons[row][col].config(
            text=player,
            state='disabled',
            disabledforeground=color
        )
        
    def check_game_end(self, player):
        """Check if game has ended (win or draw)"""
        if self.game_board.check_winner(player):
            self.game_active = False
            if self.game_mode == 'ai':
                winner_text = "You win!" if player == 'X' else "AI wins!"
            else:
                winner_text = f"Player {player} wins!"
            messagebox.showinfo("Game Over", winner_text)
            self.status_label.config(text=winner_text)
            return True
            
        if self.game_board.is_full():
            self.game_active = False
            messagebox.showinfo("Game Over", "It's a draw!")
            self.status_label.config(text="It's a draw!")
            return True
            
        return False
        
    def update_status(self):
        """Update status label"""
        player = self.game_board.current_player
        if self.game_mode == 'ai' and player == 'O':
            text = "AI's Turn"
        else:
            text = f"Player {player}'s Turn"
        self.status_label.config(text=text)
        
    def reset_game(self):
        """Reset the current game"""
        self.game_board.reset()
        self.game_active = True
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text='',
                    state='normal',
                    bg='white'
                )
                
        self.update_status()
        
    def back_to_menu(self):
        """Return to main menu"""
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.game_board.reset()
        self.game_mode = None
        self.game_active = False
        
        self.show_mode_selection()
