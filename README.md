# My Python Project Collection

A collection of four interactive Python games and applications demonstrating various programming concepts and game logic.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Projects](#projects)
  - [Project 1: Rock Paper Scissors](#project-1-rock-paper-scissors)
  - [Project 2: Blackjack Card Game](#project-2-blackjack-card-game)
  - [Project 3: Snake Water Gun](#project-3-snake-water-gun)
  - [Project 4: Number Guessing Game](#project-4-number-guessing-game)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Features](#features)
- [Contributing](#contributing)

## 🎯 Project Overview

This repository contains four Python projects that showcase different programming concepts:

- **Game Logic**: Rock Paper Scissors, Snake Water Gun, Number Guessing
- **Object-Oriented Programming**: Blackjack with Card, Deck, and Hand classes
- **User Input Handling**: Input validation and error handling
- **Random Number Generation**: Computer opponents and game mechanics
- **File I/O**: High score tracking

## 🚀 Installation

1. **Clone or download** this repository to your local machine
2. **Ensure Python 3.x** is installed on your system
3. **Navigate** to the project directory

```bash
cd My-Python-Project
```

## 🎮 Projects

### Project 1: Rock Paper Scissors

**File**: `Project 1/Rock_Paper_Game.py`

A classic Rock Paper Scissors game where you compete against the computer.

**Features:**
- Input validation for user choices
- Random computer opponent
- Clear win/lose/tie logic
- User-friendly interface

**How to Run:**
```bash
cd "Project 1"
python Rock_Paper_Game.py
```

**Game Rules:**
- Rock beats Scissors
- Paper beats Rock  
- Scissors beats Paper
- Enter your choice when prompted

### Project 2: Blackjack Card Game

**File**: `Project 2/Cards_Game.py`

A complete Blackjack implementation with object-oriented design.

**Features:**
- Full deck of 52 cards with suits and ranks
- Dealer AI with standard rules (hit on 16, stand on 17)
- Ace value handling (1 or 11)
- Multiple game sessions
- Professional card display

**How to Run:**
```bash
cd "Project 2"
python Cards_Game.py
```

**Game Rules:**
- Get as close to 21 as possible without going over
- Face cards (J, Q, K) are worth 10
- Aces are worth 1 or 11 (automatically optimized)
- Dealer must hit on 16 and below, stand on 17 and above
- Choose 'Hit' to draw a card or 'Stand' to keep your hand

### Project 3: Snake Water Gun

**File**: `Project 3/main.py`

A Snake Water Gun game (similar to Rock Paper Scissors with different elements).

**Features:**
- High score tracking system
- Simple input-based gameplay
- Score persistence in `hiscore.txt`

**How to Run:**
```bash
cd "Project 3"
python main.py
```

**Game Rules:**
- Snake beats Water
- Water beats Gun
- Gun beats Snake
- Enter 's' for Snake, 'w' for Water, 'g' for Gun

**Note**: This project appears to be incomplete and may have some issues that need fixing.

### Project 4: Number Guessing Game

**File**: `Project 4/main.py`

A number guessing game where you try to guess a random number between 1 and 100.

**Features:**
- Random number generation
- Attempt counter
- Helpful hints (higher/lower)
- Simple and addictive gameplay

**How to Run:**
```bash
cd "Project 4"
python main.py
```

**Game Rules:**
- Computer generates a random number between 1-100
- Enter your guess when prompted
- Get hints whether to guess higher or lower
- Try to guess correctly in the fewest attempts

## 📋 Requirements

- **Python 3.x** (3.6 or higher recommended)
- **No external dependencies** - all projects use only Python standard library

## 🎯 How to Run

### Quick Start

1. **Open terminal/command prompt**
2. **Navigate to the project directory:**
   ```bash
   cd /path/to/My-Python-Project
   ```

3. **Choose a project and run it:**
   ```bash
   # For Rock Paper Scissors
   cd "Project 1" && python Rock_Paper_Game.py
   
   # For Blackjack
   cd "Project 2" && python Cards_Game.py
   
   # For Snake Water Gun
   cd "Project 3" && python main.py
   
   # For Number Guessing
   cd "Project 4" && python main.py
   ```

### Running All Projects

You can run each project individually by navigating to its directory and executing the main Python file.

## ✨ Features

### Common Features Across Projects
- **Interactive gameplay** with user input
- **Error handling** for invalid inputs
- **Clear instructions** and feedback
- **Replayability** - most games can be played multiple times

### Technical Features
- **Modular code structure** (especially in Blackjack)
- **Object-oriented programming** concepts
- **File I/O operations** for score tracking
- **Random number generation** for game mechanics
- **Input validation** and user experience

## 🤝 Contributing

Feel free to contribute to these projects by:

1. **Fixing bugs** (especially in Project 3)
2. **Adding new features**
3. **Improving user interface**
4. **Adding more games**
5. **Enhancing documentation**

### Suggested Improvements
- Add graphical interfaces using libraries like `tkinter` or `pygame`
- Implement sound effects
- Add multiplayer functionality
- Create a unified game launcher
- Add configuration options
- Implement proper error handling in Project 3

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Enjoy Playing!

Each project demonstrates different Python programming concepts and provides hours of entertainment. Start with the simpler games and work your way up to the more complex Blackjack implementation!

---

**Happy Coding! 🐍🎮**
