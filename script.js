// Game State
let gameState = {
    board: ['', '', '', '', '', '', '', '', ''],
    currentPlayer: 'X',
    gameMode: null,
    gameActive: false
};

// Game Elements
const modeSelection = document.getElementById('modeSelection');
const gameBoard = document.getElementById('gameBoard');
const statusLabel = document.getElementById('statusLabel');
const modeLabel = document.getElementById('modeLabel');
const gameOverModal = document.getElementById('gameOverModal');
const gameOverMessage = document.getElementById('gameOverMessage');
const cells = document.querySelectorAll('.cell');

// Winning Combinations
const winningCombinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6]              // Diagonals
];

// Start Game
function startGame(mode) {
    gameState.gameMode = mode;
    gameState.gameActive = true;
    modeSelection.classList.add('hidden');
    gameBoard.classList.remove('hidden');
    
    const modeText = mode === 'ai' ? 'vs AI' : '2 Player';
    modeLabel.textContent = `Mode: ${modeText}`;
    updateStatus();
}

// Handle Cell Click
function handleCellClick(index) {
    if (!gameState.gameActive || gameState.board[index] !== '') {
        return;
    }
    
    makeMove(index, gameState.currentPlayer);
    
    if (checkGameEnd()) {
        return;
    }
    
    switchPlayer();
    
    // AI's turn
    if (gameState.gameMode === 'ai' && gameState.currentPlayer === 'O') {
        setTimeout(aiMove, 500);
    }
}

// Make Move
function makeMove(index, player) {
    gameState.board[index] = player;
    const cell = cells[index];
    cell.textContent = player;
    cell.classList.add('taken', player.toLowerCase());
}

// AI Move
function aiMove() {
    if (!gameState.gameActive) return;
    
    statusLabel.textContent = 'AI is thinking...';
    
    const bestMove = getBestMove();
    
    if (bestMove !== null) {
        makeMove(bestMove, 'O');
        
        if (checkGameEnd()) {
            return;
        }
        
        switchPlayer();
    }
}

// Get Best Move (Minimax)
function getBestMove() {
    let bestScore = -Infinity;
    let bestMove = null;
    
    for (let i = 0; i < 9; i++) {
        if (gameState.board[i] === '') {
            gameState.board[i] = 'O';
            let score = minimax(gameState.board, 0, false);
            gameState.board[i] = '';
            
            if (score > bestScore) {
                bestScore = score;
                bestMove = i;
            }
        }
    }
    
    return bestMove;
}

// Minimax Algorithm
function minimax(board, depth, isMaximizing) {
    const winner = checkWinnerForBoard(board);
    
    if (winner === 'O') return 10 - depth;
    if (winner === 'X') return depth - 10;
    if (isBoardFull(board)) return 0;
    
    if (isMaximizing) {
        let bestScore = -Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = 'O';
                let score = minimax(board, depth + 1, false);
                board[i] = '';
                bestScore = Math.max(score, bestScore);
            }
        }
        return bestScore;
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < 9; i++) {
            if (board[i] === '') {
                board[i] = 'X';
                let score = minimax(board, depth + 1, true);
                board[i] = '';
                bestScore = Math.min(score, bestScore);
            }
        }
        return bestScore;
    }
}

// Check Winner for Board
function checkWinnerForBoard(board) {
    for (let combo of winningCombinations) {
        const [a, b, c] = combo;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            return board[a];
        }
    }
    return null;
}

// Check Game End
function checkGameEnd() {
    const winner = checkWinnerForBoard(gameState.board);
    
    if (winner) {
        gameState.gameActive = false;
        let message;
        
        if (gameState.gameMode === 'ai') {
            message = winner === 'X' ? '🎉 You Win!' : '🤖 AI Wins!';
        } else {
            message = `🎉 Player ${winner} Wins!`;
        }
        
        showGameOver(message);
        return true;
    }
    
    if (isBoardFull(gameState.board)) {
        gameState.gameActive = false;
        showGameOver("🤝 It's a Draw!");
        return true;
    }
    
    return false;
}

// Check if Board is Full
function isBoardFull(board) {
    return board.every(cell => cell !== '');
}

// Switch Player
function switchPlayer() {
    gameState.currentPlayer = gameState.currentPlayer === 'X' ? 'O' : 'X';
    updateStatus();
}

// Update Status
function updateStatus() {
    if (!gameState.gameActive) return;
    
    let statusText;
    if (gameState.gameMode === 'ai' && gameState.currentPlayer === 'O') {
        statusText = "AI's Turn";
    } else {
        statusText = `Player ${gameState.currentPlayer}'s Turn`;
    }
    statusLabel.textContent = statusText;
}

// Show Game Over Modal
function showGameOver(message) {
    gameOverMessage.textContent = message;
    gameOverModal.classList.remove('hidden');
}

// Close Modal
function closeModal() {
    gameOverModal.classList.add('hidden');
}

// Reset Game
function resetGame() {
    gameState.board = ['', '', '', '', '', '', '', '', ''];
    gameState.currentPlayer = 'X';
    gameState.gameActive = true;
    
    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('taken', 'x', 'o');
    });
    
    updateStatus();
}

// Back to Menu
function backToMenu() {
    gameBoard.classList.add('hidden');
    modeSelection.classList.remove('hidden');
    resetGame();
    gameState.gameMode = null;
    gameState.gameActive = false;
}

// Close modal when clicking outside
gameOverModal.addEventListener('click', (e) => {
    if (e.target === gameOverModal) {
        closeModal();
    }
});
