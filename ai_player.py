"""
AI Module
Implements the minimax algorithm for intelligent gameplay
"""

class TicTacToeAI:
    def __init__(self, player='O', opponent='X'):
        self.player = player
        self.opponent = opponent
        
    def get_best_move(self, game_board):
        """Find the best move using minimax algorithm"""
        best_score = float('-inf')
        best_move = None
        
        for row, col in game_board.get_empty_cells():
            # Try this move
            temp_board = game_board.copy()
            temp_board.make_move(row, col, self.player)
            
            score = self.minimax(temp_board, 0, False)
            
            if score > best_score:
                best_score = score
                best_move = (row, col)
                
        return best_move
        
    def minimax(self, game_board, depth, is_maximizing):
        """
        Minimax algorithm with depth consideration
        Returns the best score for the current board state
        """
        # Check terminal states
        if game_board.check_winner(self.player):
            return 10 - depth
        if game_board.check_winner(self.opponent):
            return depth - 10
        if game_board.is_full():
            return 0
            
        if is_maximizing:
            # AI's turn - maximize score
            best_score = float('-inf')
            for row, col in game_board.get_empty_cells():
                temp_board = game_board.copy()
                temp_board.make_move(row, col, self.player)
                score = self.minimax(temp_board, depth + 1, False)
                best_score = max(score, best_score)
            return best_score
        else:
            # Opponent's turn - minimize score
            best_score = float('inf')
            for row, col in game_board.get_empty_cells():
                temp_board = game_board.copy()
                temp_board.make_move(row, col, self.opponent)
                score = self.minimax(temp_board, depth + 1, True)
                best_score = min(score, best_score)
            return best_score
