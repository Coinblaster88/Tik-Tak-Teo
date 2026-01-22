"""
Game Logic Module
Handles the core game state and rules for Tic-Tac-Toe
"""

class GameBoard:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
    def reset(self):
        """Reset the game board"""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
    def make_move(self, row, col, player):
        """Make a move on the board"""
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
        
    def is_valid_move(self, row, col):
        """Check if a move is valid"""
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ''
        
    def get_cell(self, row, col):
        """Get the value of a cell"""
        return self.board[row][col]
        
    def is_full(self):
        """Check if the board is full"""
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))
        
    def check_winner(self, player):
        """Check if a player has won"""
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
                
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
                
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
            
        return False
        
    def get_empty_cells(self):
        """Get list of empty cells"""
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']
        
    def copy(self):
        """Create a copy of the board"""
        new_board = GameBoard()
        new_board.board = [row[:] for row in self.board]
        new_board.current_player = self.current_player
        return new_board
        
    def switch_player(self):
        """Switch to the next player"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
