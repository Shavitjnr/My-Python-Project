# My Python Project Collection

A collection of five interactive Python projects demonstrating various programming concepts, from simple games to advanced voice-controlled virtual assistants.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Projects](#projects)
  - [Project 1: Rock Paper Scissors](#project-1-rock-paper-scissors)
  - [Project 2: Blackjack Card Game](#project-2-blackjack-card-game)
  - [Project 3: Snake Water Gun](#project-3-snake-water-gun)
  - [Project 4: Number Guessing Game](#project-4-number-guessing-game)
  - [Project 5: Jarvis Voice Assistant](#project-5-jarvis-voice-assistant)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Features](#features)
- [Contributing](#contributing)

## 🎯 Project Overview

This repository contains five Python projects that showcase different programming concepts and complexity levels:

- **Game Logic**: Rock Paper Scissors, Snake Water Gun, Number Guessing
- **Object-Oriented Programming**: Blackjack with Card, Deck, and Hand classes
- **Advanced AI & Voice Control**: Jarvis Voice Assistant with speech recognition
- **User Input Handling**: Input validation and error handling
- **Random Number Generation**: Computer opponents and game mechanics
- **File I/O**: High score tracking and data persistence
- **API Integration**: OpenAI GPT and NewsAPI integration
- **Speech Processing**: Voice recognition and text-to-speech

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

**Voice Commands:**
- **"Jarvis"** - Wake word
- **"Open Google/YouTube/Facebook/LinkedIn"** - Web browsing
- **"Play [song name]"** - Music playback
- **"News"** - Latest headlines
- **Any question** - AI-powered responses

## 📋 Requirements

### Basic Requirements (Projects 1-4)
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
   ```

### Running All Projects

You can run each project individually by navigating to its directory and executing the main Python file. Note that Project 5 requires additional setup (dependencies and API keys).

## ✨ Features

### Common Features Across Projects
- **Interactive gameplay** with user input
- **Error handling** for invalid inputs
- **Clear instructions** and feedback
- **Replayability** - most projects can be used multiple times

### Technical Features
- **Modular code structure** (especially in Blackjack and Jarvis)
- **Object-oriented programming** concepts
- **File I/O operations** for data persistence
- **Random number generation** for game mechanics
- **Input validation** and user experience
- **API integration** (Project 5)
- **Speech recognition and synthesis** (Project 5)
- **Web automation** (Project 5)

### Project Complexity Progression
1. **Project 1**: Basic game logic and input handling
2. **Project 2**: Object-oriented design and complex game rules
3. **Project 3**: File I/O and score tracking
4. **Project 4**: Random generation and user feedback
5. **Project 5**: Advanced AI, speech processing, and API integration

## 🤝 Contributing

Feel free to contribute to these projects by:

1. **Fixing bugs** (especially in Project 3)
2. **Adding new features**
3. **Improving user interface**
4. **Adding more games or assistant features**
5. **Enhancing documentation**
6. **Expanding Jarvis capabilities**

### Suggested Improvements
- Add graphical interfaces using libraries like `tkinter` or `pygame`
- Implement sound effects for games
- Add multiplayer functionality
- Create a unified game launcher
- Add configuration options
- Implement proper error handling in Project 3
- Expand Jarvis with more voice commands
- Add home automation features to Jarvis
- Implement offline speech recognition
- Add multi-language support to Jarvis

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Enjoy Your Python Journey!

This collection demonstrates the evolution of Python programming concepts, from simple games to advanced AI-powered applications. Start with the basic games to learn fundamentals, then explore the sophisticated voice assistant to see Python's full potential!

---

**Happy Coding! 🐍🎮🤖**
