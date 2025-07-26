# Project 8: Ludo Game (CLI Edition)

A simple, interactive command-line Ludo game for 2-4 players. Each player rolls a dice in turn, and the first to reach the target position wins!

## 📋 Project Overview
This project is a Python implementation of a basic Ludo-style race game. Players take turns rolling a dice, advancing their token along a virtual board. The game demonstrates user input handling, random number generation, turn-based logic, and simple state management in Python.

## ✨ Features
- 2 to 4 player support (custom player names)
- Each player is assigned a classic Ludo color (Red, Blue, Green, Yellow)
- Turn-based dice rolling (random 1-6)
- Progress tracking for each player
- Announces the winner and ends the game
- User-friendly command-line prompts

## 🛠️ Technologies Used
- **Python 3.x**
- Standard library only (`random` and `input`)

## 🚀 How to Run
1. **Open a terminal** and navigate to the Project 8 directory:
   ```bash
   cd "Project 8"
   ```
2. **Run the game using Python 3:**
   ```bash
   python ludo_game.py
   ```
3. **Follow the on-screen prompts:**
   - Enter the number of players (2-4)
   - Enter each player's name
   - Press Enter to roll the dice on your turn
   - Watch your progress and see who wins!

## 📝 Example Session
```
Enter number of players (2-4): 3
Enter name for Player 1: Alice
Enter name for Player 2: Bob
Enter name for Player 3: Carol

🎲 LUDO GAME STARTS! First to reach position 50 wins!

Alice (Red), press Enter to roll the dice...
🎲 Alice rolled a 4!
Alice's new position: 4

Bob (Blue), press Enter to roll the dice...
🎲 Bob rolled a 6!
Bob's new position: 6

Carol (Green), press Enter to roll the dice...
🎲 Carol rolled a 2!
Carol's new position: 2

... (game continues) ...

🏆 Bob (Blue) wins the game!
```

## 💡 Professional Tips
- Make sure you have Python 3 installed (`python --version`)
- Run the script from the command line for best results
- The game uses only standard Python modules—no installation required
- To stop the game at any time, press `Ctrl+C`

## 🤝 Contributing
Suggestions for improvement:
- Add support for snakes/ladders or obstacles
- Implement a graphical interface (e.g., with `tkinter`)
- Add sound effects or animations
- Allow custom target positions
- Track and display a leaderboard

## 📝 License
This project is open source and available under the MIT License.
