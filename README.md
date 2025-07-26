# My Python Project Collection

A collection of eight interactive Python projects demonstrating a range of programming concepts, from classic games to utilities and AI-powered assistants.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Project Summaries](#project-summaries)
  - [Project 1: Rock Paper Scissors](#project-1-rock-paper-scissors)
  - [Project 2: Blackjack Card Game](#project-2-blackjack-card-game)
  - [Project 3: Snake Water Gun](#project-3-snake-water-gun)
  - [Project 4: Number Guessing Game](#project-4-number-guessing-game)
  - [Project 5: Jarvis Voice Assistant](#project-5-jarvis-voice-assistant)
  - [Project 6: Rent Calculator](#project-6-rent-calculator)
  - [Project 7: Coin Toss Game](#project-7-coin-toss-game)
  - [Project 8: Ludo Game](#project-8-ludo-game)
- [Requirements Summary](#requirements-summary)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview
This repository contains the following Python projects:

## Project Summaries

### Project 1: Rock Paper Scissors
- **Description:** Classic game against the computer with input validation and clear win/lose logic.
- **Features:** User vs. computer, random choices, input validation.
- **Python Version:** 3.6+
- **Libraries:** Standard library only
- **How to Run:**
  ```bash
  cd "Project 1"
  python Rock_Paper_Game.py
  ```

### Project 2: Blackjack Card Game
- **Description:** OOP-based Blackjack with dealer AI, full deck, and ace value handling.
- **Features:** Multiple sessions, professional card display, dealer AI.
- **Python Version:** 3.6+
- **Libraries:** Standard library only
- **How to Run:**
  ```bash
  cd "Project 2"
  python Cards_Game.py
  ```

### Project 3: Snake Water Gun
- **Description:** A variant of Rock Paper Scissors with score tracking and file I/O.
- **Features:** High score tracking, simple input-based gameplay.
- **Python Version:** 3.6+
- **Libraries:** Standard library only
- **How to Run:**
  ```bash
  cd "Project 3"
  python main.py
  ```

### Project 4: Number Guessing Game
- **Description:** Guess a random number between 1 and 100 with hints and attempt counter.
- **Features:** Random number generation, hints, replayability.
- **Python Version:** 3.6+
- **Libraries:** Standard library only
- **How to Run:**
  ```bash
  cd "Project 4"
  python main.py
  ```

### Project 5: Jarvis Voice Assistant
- **Description:** Voice-controlled AI assistant with web, music, and news features.
- **Features:** Voice control, web automation, music playback, news updates, OpenAI GPT integration, text-to-speech.
- **Python Version:** 3.7+
- **Libraries:**
  - `speechrecognition>=3.8.1`
  - `pyttsx3>=2.90`
  - `openai>=0.27.0`
  - `requests>=2.25.1`
  - `python-dotenv>=0.19.0`
  - `pyaudio>=0.2.11`
  - See `Project 5/requirements.txt` for full list
- **How to Run:**
  ```bash
  cd "Project 5"
  pip install -r requirements.txt
  # Set up .env file with API keys (see README copy.md)
  python main.py
  ```

### Project 6: Rent Calculator
- **Description:** Utility to split rent, food, and electricity costs among roommates.
- **Features:** User-friendly prompts, fair cost splitting, simple CLI.
- **Python Version:** 3.6+
- **Libraries:** Standard library only
- **How to Run:**
  ```bash
  cd "Project 6"
  python rent_calculator.py
  ```

### Project 7: Coin Toss Game
- **Description:** Interactive CLI game where users guess heads or tails, with score tracking.
- **Features:** Random coin toss, user guesses, score tracking, replay option.
- **Python Version:** 3.6+
- **Libraries:** Standard library only (`random`)
- **How to Run:**
  ```bash
  cd "Project 7"
  python coin_toss_game.py
  ```

### Project 8: Ludo Game
- **Description:** Command-line Ludo-style race game for 2-4 players. Roll dice, race to the finish!
- **Features:** 2-4 players, color assignment, turn-based dice rolling, winner announcement.
- **Python Version:** 3.6+
- **Libraries:** Standard library only (`random`)
- **How to Run:**
  ```bash
  cd "Project 8"
  python ludo_game.py
  ```

## 🗂️ Requirements Summary
| Project         | Python Version | Extra Libraries/Dependencies         |
|----------------|---------------|--------------------------------------|
| Project 1      | 3.6+          | None                                 |
| Project 2      | 3.6+          | None                                 |
| Project 3      | 3.6+          | None                                 |
| Project 4      | 3.6+          | None                                 |
| Project 5      | 3.7+          | See requirements.txt (Project 5)     |
| Project 6      | 3.6+          | None                                 |
| Project 7      | 3.6+          | None                                 |
| Project 8      | 3.6+          | None                                 |

## 🚀 How to Run
1. **Install Python 3.6+** (3.7+ for Project 5)
2. **Clone this repository**
3. **Navigate to the desired project folder**
4. **Run the main Python file** as shown above
5. **For Project 5:** Install dependencies and set up API keys as described in its README

## 🤝 Contributing
Contributions are welcome! You can:
- Fix bugs or add features
- Improve user interfaces
- Add new games or utilities
- Enhance documentation
- Submit pull requests for review

## 📝 License
MIT License. See LICENSE file for details.
