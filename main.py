#!/usr/bin/env python3
"""
Tic-Tac-Toe Game
Main entry point for the application

Features:
- Play against AI (with minimax algorithm)
- Play against a friend (2-player mode)
"""

import tkinter as tk
from ui_interface import TicTacToeUI

def main():
    """Initialize and run the game"""
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
