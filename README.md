# My Python Project Collection

A collection of six interactive Python projects demonstrating various programming concepts, from simple games to advanced voice-controlled virtual assistants and practical utilities.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Projects](#projects)
  - [Project 1: Rock Paper Scissors](#project-1-rock-paper-scissors)
  - [Project 2: Blackjack Card Game](#project-2-blackjack-card-game)
  - [Project 3: Snake Water Gun](#project-3-snake-water-gun)
  - [Project 4: Number Guessing Game](#project-4-number-guessing-game)
  - [Project 5: Jarvis Voice Assistant](#project-5-jarvis-voice-assistant)
  - [Project 6: Rent Calculator](#project-6-rent-calculator)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Features](#features)
- [Contributing](#contributing)

## 🎯 Project Overview

This repository contains six Python projects that showcase different programming concepts and complexity levels:

- **Game Logic**: Rock Paper Scissors, Snake Water Gun, Number Guessing
- **Object-Oriented Programming**: Blackjack with Card, Deck, and Hand classes
- **Advanced AI & Voice Control**: Jarvis Voice Assistant with speech recognition
- **User Input Handling**: Input validation and error handling
- **Random Number Generation**: Computer opponents and game mechanics
- **File I/O**: High score tracking and data persistence
- **API Integration**: OpenAI GPT and NewsAPI integration
- **Speech Processing**: Voice recognition and text-to-speech
- **Practical Utilities**: Rent Calculator for splitting costs

## 🚀 Installation

1. **Clone or download** this repository to your local machine
2. **Ensure Python 3.x** is installed on your system (3.7+ recommended for Project 5)
3. **Navigate** to the project directory

```bash
cd My-Python-Project
```

4. **For Project 5 (Jarvis)**: Install additional dependencies and set up API keys
   ```bash
   cd "Project 5"
   pip install -r requirements.txt
   # Create .env file with API keys (see Project 5 documentation)
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

### Project 5: Jarvis Voice Assistant

**File**: `Project 5/main.py`

A sophisticated voice-controlled virtual assistant inspired by Iron Man's JARVIS.

**Features:**
- 🎤 **Voice Control**: Wake word detection ("Jarvis")
- 🌐 **Web Automation**: Open websites with voice commands
- 🎵 **Music Playback**: Voice-controlled YouTube music
- 📰 **News Updates**: Real-time news headlines
- 🤖 **AI Integration**: OpenAI GPT-powered responses
- 🔊 **Text-to-Speech**: Natural voice responses

**Requirements:**
- Microphone and speakers
- Internet connection
- OpenAI API key
- NewsAPI key

**How to Run:**
```bash
cd "Project 5"
pip install -r requirements.txt
# Set up .env file with API keys
python main.py
```

### Project 6: Rent Calculator

**File**: `Project 6/rent_calculator.py`

A simple command-line tool to split rent and utility costs among roommates or flatmates.

**Features:**
- User-friendly prompts for all required inputs
- Calculates each person's share of rent, food, and electricity
- Simple integer division for fair splitting

**How to Run:**
```bash
cd "Project 6"
python rent_calculator.py
```

**Example:**
```
Enter your hostel/flat rent = 12000
Enter the amount of food ordered = 3000
Enter the total of electricity spend = 150
Enter the charge per unit = 8
Enter the number of persons living in room/flat = 4
Each person will pay = 4050
```

## 📋 Requirements

### Basic Requirements (Projects 1-4, 6)
- **Python 3.x** (3.6 or higher)
- **No external dependencies** - uses only Python standard library

### Advanced Requirements (Project 5)
- **Python 3.7+** (recommended)
- **Microphone and speakers**
- **Internet connection**
- **API keys**: OpenAI and NewsAPI
- **Dependencies**: See `Project 5/requirements.txt`

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
   
   # For Jarvis Voice Assistant
   cd "Project 5" && python main.py
   
   # For Rent Calculator
   cd "Project 6" && python rent_calculator.py
   ```

### Running All Projects

You can run each project individually by navigating to its directory and executing the main Python file. Note that Project 5 requires additional setup (dependencies and API keys).

## ✨ Features

### Common Features Across Projects
- **Interactive gameplay or utility** with user input
- **Error handling** for invalid inputs
- **Clear instructions** and feedback
- **Replayability** or reusability

### Technical Features
- **Modular code structure** (especially in Blackjack and Jarvis)
- **Object-oriented programming** concepts
- **File I/O operations** for data persistence
- **Random number generation** for game mechanics
- **Input validation** and user experience
- **API integration** (Project 5)
- **Speech recognition and synthesis** (Project 5)
- **Web automation** (Project 5)
- **Practical utilities** (Project 6)

### Project Complexity Progression
1. **Project 1**: Basic game logic and input handling
2. **Project 2**: Object-oriented design and complex game rules
3. **Project 3**: File I/O and score tracking
4. **Project 4**: Random generation and user feedback
5. **Project 5**: Advanced AI, speech processing, and API integration
6. **Project 6**: Practical utility for daily life

## 🤝 Contributing

Feel free to contribute to these projects by:

1. **Fixing bugs** (especially in Project 3)
2. **Adding new features**
3. **Improving user interface**
4. **Adding more games, utilities, or assistant features**
5. **Enhancing documentation**
6. **Expanding Jarvis capabilities**
7. **Improving the Rent Calculator (input validation, decimals, GUI, etc.)**

### Suggested Improvements
- Add graphical interfaces using libraries like `tkinter` or `pygame`
- Implement sound effects for games
- Add multiplayer functionality
- Create a unified game launcher
- Add configuration options
- Implement proper error handling in Project 3 and 6
- Expand Jarvis with more voice commands
- Add home automation features to Jarvis
- Implement offline speech recognition
- Add multi-language support to Jarvis
- Add more practical utilities

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Enjoy Your Python Journey!

This collection demonstrates the evolution of Python programming concepts, from simple games to advanced AI-powered applications and practical tools. Start with the basic games to learn fundamentals, then explore the sophisticated voice assistant and utilities to see Python's full potential!

---

**Happy Coding! 🐍🎮🤖**
