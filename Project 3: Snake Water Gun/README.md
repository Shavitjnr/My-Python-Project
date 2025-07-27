# Snake Water Gun Game

A Python implementation of the Snake Water Gun game (similar to Rock Paper Scissors) featuring high score tracking and file-based persistence.

## Overview

This project implements a variation of the classic Rock Paper Scissors game using different elements: Snake, Water, and Gun. The game includes basic scoring functionality with persistent high score tracking through file I/O operations. Note: This implementation is currently in development and may require additional refinement.

## Project Structure

```
Project 3/
├── main.py        # Main game implementation
├── hiscore.txt    # High score persistence file
└── README.md      # Project documentation
```

## Requirements

- **Python**: 3.6 or higher
- **Dependencies**: None (uses only Python standard library)
- **Platform**: Cross-platform (Windows, macOS, Linux)
- **File Permissions**: Read/write access for score tracking

## Installation

1. Ensure Python 3.x is installed on your system
2. Clone or download this project
3. Navigate to the Project 3 directory

## Usage

### Running the Game

```bash
# Navigate to project directory
cd "Project 3"

# Execute the game
python main.py
```

### Alternative Execution Methods

```bash
# Using python3 explicitly
python3 main.py

# From parent directory
python "Project 3/main.py"

# With executable permissions (Linux/macOS)
chmod +x main.py
./main.py
```

## Game Mechanics

### Snake Water Gun Rules
- **Snake** defeats **Water**
- **Water** defeats **Gun**
- **Gun** defeats **Snake**
- Identical choices result in a tie

### Gameplay Flow
1. Player enters their choice (s, w, g)
2. Computer generates a predetermined choice
3. Game logic determines the winner
4. Score is tracked and persisted

### Player Input
- **'s'**: Snake
- **'w'**: Water  
- **'g'**: Gun
- Input is case-sensitive

## Code Architecture

### Current Implementation

```python
# Game logic structure
computer = -1  # Fixed computer choice (Water)
me = int(input("Enter your Choice: "))
you = {"s":1,"w":-1,"g":0}  # Choice mapping
```

### Core Components

#### Input Processing
- **User Input**: Integer-based choice selection
- **Choice Mapping**: Dictionary-based value assignment
- **Computer Opponent**: Fixed choice implementation

#### Score Management
- **File I/O**: High score persistence in `hiscore.txt`
- **Score Tracking**: Basic numerical scoring system
- **Data Persistence**: Cross-session score maintenance

### Design Considerations
- **Simple Logic**: Basic win/lose determination
- **File Operations**: Score persistence implementation
- **Input Handling**: Integer-based choice system
- **Fixed Opponent**: Deterministic computer behavior

## Technical Specifications

| Specification | Value |
|---------------|-------|
| Language | Python 3.x |
| File Size | ~339B |
| Lines of Code | 18 |
| Dependencies | Standard library only |
| Complexity | Basic |
| Architecture | Procedural |

## Current Implementation Status

### Working Features
- Basic game logic implementation
- High score file creation and reading
- Simple input/output functionality
- Core win/lose determination

### Known Issues
- **Incomplete Game Logic**: Missing final comparison logic
- **Fixed Computer Choice**: Computer always chooses Water (-1)
- **Limited Input Validation**: No error handling for invalid inputs
- **Incomplete Score System**: Score tracking not fully implemented

### Development Notes
The current implementation shows the foundation for a Snake Water Gun game but requires additional development to be fully functional. The code demonstrates basic Python concepts including file I/O, dictionary usage, and simple game logic.

## Example Session

```
Enter your Choice: s
# Game logic processing
# Score tracking (incomplete)
```

## Development

### Code Quality Assessment
- **Basic Structure**: Foundation for game implementation
- **File I/O**: High score persistence mechanism
- **Simple Logic**: Core game rules implementation
- **Learning Value**: Demonstrates fundamental Python concepts

### Areas for Improvement
- Complete game logic implementation
- Add input validation and error handling
- Implement random computer opponent
- Enhance score tracking system
- Add user-friendly interface

### Best Practices to Implement
- Input validation and error recovery
- Random number generation for computer choices
- Comprehensive game state management
- User-friendly output formatting
- Robust file I/O error handling

## Troubleshooting

### Common Issues

**Python Command Not Found**
```bash
# Install Python from official website
# https://www.python.org/downloads/

# Or use python3 explicitly
python3 main.py
```

**Permission Denied (Linux/macOS)**
```bash
# Grant execute permissions
chmod +x main.py
```

**File Permission Issues**
```bash
# Ensure write permissions for score file
chmod 644 hiscore.txt
```

**Game Logic Issues**
- Current implementation is incomplete
- Computer choice is fixed (always Water)
- Final comparison logic needs completion

## Future Enhancements

### Critical Improvements Needed
- Complete the game logic implementation
- Add random computer opponent
- Implement proper input validation
- Enhance score tracking system
- Add user-friendly interface

### Potential Features
- Multiple game rounds
- Statistics tracking
- Enhanced scoring system
- Graphical user interface
- Sound effects and animations
- Tournament mode

### Technical Upgrades
- Object-oriented redesign
- Database integration for scores
- Web-based interface
- Machine learning opponent
- Performance optimization
- Comprehensive testing suite

## Contributing

This project welcomes contributions in the following areas:
- **Critical**: Complete the game logic implementation
- **Important**: Add input validation and error handling
- **Enhancement**: Implement random computer opponent
- **Feature**: Improve score tracking and statistics
- **Quality**: Add comprehensive testing
- **Documentation**: Enhance code comments and documentation

## Development Roadmap

### Phase 1: Core Functionality
- Complete game logic implementation
- Add random computer opponent
- Implement basic input validation

### Phase 2: User Experience
- Enhance user interface
- Improve score tracking
- Add game statistics

### Phase 3: Advanced Features
- Multiple game modes
- Tournament system
- Performance optimization

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions:
1. Review the current implementation status
2. Check the troubleshooting section above
3. Ensure Python 3.x is properly installed
4. Verify file permissions for score tracking
5. Note that this is a development project requiring completion

---

**Version**: 0.1 (Development)  
**Last Updated**: 2025  
**Maintainer**: Python Project Collection  
**Status**: In Development
