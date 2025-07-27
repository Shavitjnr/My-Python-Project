# Blackjack Card Game

A sophisticated Python implementation of the classic Blackjack card game featuring object-oriented design, complete deck management, and professional game logic.

## Overview

This project demonstrates advanced Python programming concepts through a fully-featured Blackjack implementation. The game includes a complete 52-card deck, dealer AI with standard casino rules, ace value optimization, and comprehensive game state management using object-oriented programming principles.

## Project Structure

```
Project 2/
├── Cards_Game.py    # Complete Blackjack implementation
└── README.md       # Project documentation
```

## Requirements

- **Python**: 3.6 or higher
- **Dependencies**: None (uses only Python standard library)
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **Memory**: Minimal (text-based interface)

## Installation

1. Ensure Python 3.x is installed on your system
2. Clone or download this project
3. Navigate to the Project 2 directory

## Usage

### Running the Game

```bash
# Navigate to project directory
cd "Project 2"

# Execute the game
python Cards_Game.py
```

### Alternative Execution Methods

```bash
# Using python3 explicitly
python3 Cards_Game.py

# From parent directory
python "Project 2/Cards_Game.py"

# With executable permissions (Linux/macOS)
chmod +x Cards_Game.py
./Cards_Game.py
```

## Game Mechanics

### Blackjack Rules
- **Objective**: Get as close to 21 as possible without exceeding it
- **Card Values**:
  - Number cards (2-10): Face value
  - Face cards (J, Q, K): 10 points each
  - Aces: 1 or 11 points (automatically optimized)
- **Dealer Rules**: Must hit on 16 and below, stand on 17 and above
- **Winning**: Beat the dealer's hand without busting

### Gameplay Flow
1. Player specifies number of games to play
2. Each game begins with two cards dealt to player and dealer
3. Player chooses to "Hit" (draw card) or "Stand" (keep current hand)
4. Dealer plays according to standard rules
5. Winner is determined based on hand values
6. Game continues for specified number of rounds

### Player Actions
- **Hit**: Draw an additional card to your hand
- **Stand**: Keep your current hand and end your turn
- **Input**: Accepts "hit", "h", "stand", or "s" (case-insensitive)

## Code Architecture

### Object-Oriented Design

```python
class Card:
    """Represents a single playing card with suit and rank"""
    
class Deck:
    """Manages a complete 52-card deck with shuffling and dealing"""
    
class Hand:
    """Represents a player's or dealer's hand with value calculation"""
    
class Game:
    """Orchestrates the complete Blackjack game flow"""
```

### Core Components

#### Card Class
- **Properties**: suit, rank (with value)
- **Methods**: `__str__()` for card display
- **Features**: Complete card representation

#### Deck Class
- **Properties**: 52-card collection
- **Methods**: `shuffle()`, `deal(number)`
- **Features**: Standard deck with all suits and ranks

#### Hand Class
- **Properties**: cards list, calculated value, dealer flag
- **Methods**: `add_card()`, `calculate_value()`, `display()`
- **Features**: Ace optimization, dealer card hiding

#### Game Class
- **Properties**: Game state management
- **Methods**: `play()`, `check_winner()`
- **Features**: Complete game orchestration

### Design Patterns
- **Encapsulation**: Each class manages its own data and behavior
- **Inheritance**: Extensible design for future enhancements
- **Polymorphism**: Consistent interface across different hand types
- **Single Responsibility**: Each class has a focused purpose

## Technical Specifications

| Specification | Value |
|---------------|-------|
| Language | Python 3.x |
| File Size | ~5.7KB |
| Lines of Code | 184 |
| Dependencies | Standard library only |
| Complexity | Intermediate |
| Architecture | Object-Oriented |

## Example Session

```
How many games do you want to play? 2

******************************
Game 1 of 2
******************************
Your hand:
A of hearts
7 of diamonds
Value: 18

Dealer's hand:
hidden
K of clubs

Please choose 'Hit' or 'Stand': stand

Dealer's hand:
Q of spades
K of clubs
Value: 20

Final Results
Your hand: 18
Dealer's hand: 20
Dealer wins. 😭

******************************
Game 2 of 2
******************************
...
```

## Development

### Code Quality
- **Object-Oriented Design**: Clean class structure and relationships
- **Error Handling**: Robust input validation and game state management
- **Code Documentation**: Clear class and method purposes
- **Maintainability**: Modular, extensible architecture

### Best Practices Implemented
- Proper class design with encapsulation
- Consistent naming conventions
- Comprehensive input validation
- Efficient data structures
- Professional game logic implementation

### Advanced Features
- **Ace Value Optimization**: Automatic 1/11 value adjustment
- **Dealer AI**: Standard casino rules implementation
- **Card Display Logic**: Hidden dealer cards until reveal
- **Game State Management**: Complete round tracking
- **Input Flexibility**: Multiple input format acceptance

## Troubleshooting

### Common Issues

**Python Command Not Found**
```bash
# Install Python from official website
# https://www.python.org/downloads/

# Or use python3 explicitly
python3 Cards_Game.py
```

**Permission Denied (Linux/macOS)**
```bash
# Grant execute permissions
chmod +x Cards_Game.py
```

**Invalid Input Handling**
- Game accepts: "hit", "h", "stand", "s"
- Case-insensitive input processing
- Continuous prompting for invalid inputs

**Game Logic Questions**
- Dealer must hit on 16 and below
- Aces automatically optimize to prevent busting
- Blackjack (21) is an automatic win

## Future Enhancements

### Potential Improvements
- Betting system with chip management
- Multiple deck support
- Player statistics and history
- Advanced dealer AI strategies
- Card counting detection
- Tournament mode
- Network multiplayer functionality

### Technical Upgrades
- Database integration for persistent statistics
- Web-based interface development
- Machine learning for dealer AI
- Performance optimization for large-scale play
- Unit testing and test coverage
- Configuration management system

## Contributing

This project welcomes contributions in the following areas:
- Advanced game features and betting systems
- Performance optimization and code refactoring
- Additional game modes and variations
- Enhanced user interface and experience
- Testing and quality assurance improvements
- Documentation and code comments

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions:
1. Review the troubleshooting section above
2. Examine the class structure and method implementations
3. Ensure Python 3.x is properly installed
4. Verify file permissions and execution rights
5. Check game rules and logic for clarification

---

**Version**: 1.0  
**Last Updated**: 2025  
**Maintainer**: Python Project Collection
