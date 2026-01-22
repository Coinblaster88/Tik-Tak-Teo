# Tic-Tac-Toe Game

A Python-based Tic-Tac-Toe game with two game modes:
- **Play vs AI**: Challenge an intelligent AI opponent that uses the minimax algorithm
- **2 Player Mode**: Play face-to-face with a friend

## Features

- 🎮 Intuitive graphical interface using tkinter
- 🤖 Smart AI opponent that never loses (uses minimax algorithm)
- 👥 Two-player local multiplayer mode
- 🔄 Easy reset and mode switching
- 🎨 Clean and user-friendly design
- 📦 Modular code structure with separate components

## Project Structure

```
Tik-Tak-Teo/
├── Python Version:
│   ├── main.py           # Main entry point
│   ├── game_logic.py     # Game board logic and rules
│   ├── ai_player.py      # AI implementation (minimax algorithm)
│   ├── ui_interface.py   # User interface (tkinter)
│   └── tictactoe.py      # Original monolithic version (legacy)
│
├── Web Version:
│   ├── index.html        # HTML structure
│   ├── style.css         # Styling
│   └── script.js         # Game logic and AI
│
└── README.md             # Documentation
```

## Requirements

### Python Version
- Python 3.x
- tkinter (usually comes pre-installed with Python)

### Web Version
- Any modern web browser (Chrome, Firefox, Safari, Edge)

## How to Run

### Python Version
```bash
# Run the modular version
python3 main.py

# Or run the original version
python3 tictactoe.py
```

### Web Version
Simply open `index.html` in your web browser, or use a local server:
```bash
# Using Python's built-in server
python3 -m http.server 8000
# Then visit: http://localhost:8000
```

## How to Play

1. Launch the game and choose your game mode:
   - **Play vs AI**: You play as X, AI plays as O
   - **2 Player Mode**: Take turns playing X and O

2. Click on any empty cell to make your move

3. The first player to get 3 in a row (horizontally, vertically, or diagonally) wins!

4. Use the **Reset** button to start a new game or **Main Menu** to change game mode

## Game Rules

- Player X always goes first
- Players alternate turns
- The game ends when:
  - A player gets 3 in a row (winner)
  - All cells are filled (draw)

Enjoy the game!
