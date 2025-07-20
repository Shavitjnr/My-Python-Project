# Jarvis - Voice-Controlled Virtual Assistant

A Python-based voice-controlled virtual assistant inspired by Iron Man's JARVIS, featuring speech recognition, text-to-speech, web automation, music playback, news fetching, and AI-powered responses.

## Overview

Jarvis is an intelligent virtual assistant that responds to voice commands and performs various tasks including web browsing, music playback, news updates, and general AI-powered conversations. The system uses wake word detection ("Jarvis") to activate and processes natural language commands through multiple integrated services.

## Project Structure

```
Project 5/
├── main.py              # Main Jarvis assistant implementation
├── client.py            # OpenAI API client for AI responses
├── musicLibrary.py      # Music library with YouTube URLs
├── test_songs.py        # Testing utility for music functionality
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── README copy.md      # This documentation file
```

## Features

### 🎤 Voice Control
- **Wake Word Detection**: Activates with "Jarvis" command
- **Speech Recognition**: Converts voice to text using Google Speech Recognition
- **Text-to-Speech**: Responds with natural voice using gTTS and Pygame

### 🌐 Web Automation
- **Browser Control**: Opens websites with voice commands
- **Supported Sites**: Google, Facebook, YouTube, LinkedIn
- **Extensible**: Easy to add more websites

### 🎵 Music Playback
- **Voice-Controlled Music**: "Play [song name]" commands
- **YouTube Integration**: Direct YouTube video playback
- **Music Library**: Curated collection of songs with easy expansion

### 📰 News Updates
- **Real-time News**: Fetches latest headlines from NewsAPI
- **Voice Reading**: Reads news headlines aloud
- **Country-specific**: Currently configured for Indian news

### 🤖 AI Integration
- **OpenAI GPT Integration**: Intelligent responses to complex queries
- **Natural Language Processing**: Understands and responds to natural speech
- **Contextual Responses**: Maintains conversation context

## Requirements

### System Requirements
- **Python**: 3.7 or higher
- **Microphone**: Working microphone for voice input
- **Speakers**: Audio output for voice responses
- **Internet Connection**: Required for API calls and web features

### API Keys Required
- **OpenAI API Key**: For AI-powered responses
- **NewsAPI Key**: For news fetching functionality

### Dependencies
```
SpeechRecognition==3.14.3
pyttsx3==2.99
requests==2.32.4
openai==1.10.0
gTTS==2.5.4
pygame==2.6.1
PyAudio==0.2.14
python-dotenv==1.0.1
```

## Installation

### 1. Clone or Download the Project
```bash
# Navigate to project directory
cd "My-Python-Project/Project 5"
```

### 2. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Set Up API Keys
Create a `.env` file in the project directory:
```bash
# Create .env file
touch .env
```

Add your API keys to the `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_newsapi_key_here
```

### 4. Test Installation
```bash
# Test the music library
python test_songs.py

# Run the main assistant
python main.py
```

## Usage

### Starting Jarvis
```bash
python main.py
```

### Voice Commands

#### Basic Commands
- **"Jarvis"** - Wake word to activate the assistant
- **"Open Google"** - Opens Google in default browser
- **"Open YouTube"** - Opens YouTube in default browser
- **"Open Facebook"** - Opens Facebook in default browser
- **"Open LinkedIn"** - Opens LinkedIn in default browser

#### Music Commands
- **"Play skyfall"** - Plays Skyfall from YouTube
- **"Play moonlight"** - Plays Moonlight from YouTube
- **"Play 11K"** - Plays 11K from YouTube
- **"Play raat rani"** - Plays Raat Rani from YouTube
- **"Play sad ganna"** - Plays Sad Ganna from YouTube
- **"Play jhol"** - Plays Jhol from YouTube
- **"Play with you"** - Plays With You from YouTube
- **"Play let the world burn"** - Plays Let the World Burn from YouTube
- **"Play make the angels cry"** - Plays Make the Angels Cry from YouTube

#### Information Commands
- **"News"** - Fetches and reads latest news headlines
- **Any other question** - Gets AI-powered response from OpenAI

### Example Session
```
User: "Jarvis"
Jarvis: "Ya"
User: "Play skyfall"
Jarvis: "Playing Skyfall from YouTube..."
[Opens YouTube video]

User: "Jarvis"
Jarvis: "Ya"
User: "What's the weather like?"
Jarvis: [AI-powered response about weather]
```

## Technical Architecture

### Core Components

#### Speech Recognition (`main.py`)
```python
# Wake word detection
if(word.lower() == "jarvis"):
    speak("Ya")
    # Listen for command
    command = r.recognize_google(audio)
    processCommand(command)
```

#### Command Processing (`processCommand()`)
- **Web Commands**: Direct browser automation
- **Music Commands**: YouTube integration via music library
- **News Commands**: NewsAPI integration
- **AI Commands**: OpenAI GPT integration

#### Text-to-Speech (`speak()`)
```python
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
```

### Music Library System
The `musicLibrary.py` contains a dictionary of songs with YouTube URLs:
```python
music = {
    "skyfall": "https://youtu.be/DeumyOzKqgI?si=yIQr1l8F-ISWalPl",
    "moonlight": "https://youtu.be/RC_yQ7-rt6Q?si=MaIGCoqlKj23HKul",
    # ... more songs
}
```

### AI Integration
Uses OpenAI's GPT-3.5-turbo for intelligent responses:
```python
def aiProcess(command):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis..."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content
```

## Configuration

### Environment Variables
Create a `.env` file with:
```env
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_newsapi_key_here
```

### Customizing Music Library
Edit `musicLibrary.py` to add or modify songs:
```python
music = {
    "your_song_name": "youtube_url_here",
    # Add more songs as needed
}
```

### Adding New Web Commands
Modify the `processCommand()` function in `main.py`:
```python
elif "open your_site" in c.lower():
    webbrowser.open("https://yoursite.com")
```

## Troubleshooting

### Common Issues

**Microphone Not Working**
```bash
# Install PyAudio dependencies (Ubuntu/Debian)
sudo apt-get install python3-pyaudio portaudio19-dev

# macOS
brew install portaudio

# Windows
pip install PyAudio
```

**Speech Recognition Issues**
- Ensure microphone is properly connected and working
- Check internet connection (required for Google Speech Recognition)
- Speak clearly and in a quiet environment

**API Key Errors**
```bash
# Check if .env file exists and contains correct keys
cat .env

# Verify API keys are valid
python client.py
```

**Audio Playback Issues**
- Ensure speakers/headphones are connected
- Check system audio settings
- Verify pygame installation

### Error Messages

**"No module named 'speech_recognition'"**
```bash
pip install SpeechRecognition
```

**"No module named 'pygame'"**
```bash
pip install pygame
```

**"OpenAI API quota exceeded"**
- Check your OpenAI account billing
- Verify API key is correct
- Consider upgrading your OpenAI plan

## Testing

### Test Music Library
```bash
python test_songs.py
```

This will:
- Display all available songs
- Test song search functionality
- Verify YouTube URLs are accessible

### Test OpenAI Integration
```bash
python client.py
```

This will:
- Test OpenAI API connection
- Provide mock response if API quota exceeded
- Verify environment variable setup

## Development

### Adding New Features

#### New Voice Commands
1. Add condition in `processCommand()` function
2. Implement the command logic
3. Test with voice input

#### New Music Songs
1. Add song to `musicLibrary.py`
2. Test with `test_songs.py`
3. Verify YouTube URL accessibility

#### New Web Services
1. Add new API integration
2. Implement error handling
3. Add voice command trigger

### Code Structure
- **Modular Design**: Separate files for different functionalities
- **Error Handling**: Try-catch blocks for robust operation
- **Environment Variables**: Secure API key management
- **Extensible Architecture**: Easy to add new features

## Security Considerations

### API Key Management
- Never commit API keys to version control
- Use environment variables for sensitive data
- Regularly rotate API keys

### Privacy
- Voice data is processed by Google Speech Recognition
- OpenAI processes conversation data
- Consider privacy implications for voice recordings

## Future Enhancements

### Planned Features
- **Home Automation**: Control smart home devices
- **Calendar Integration**: Schedule management
- **Email Management**: Voice-controlled email
- **Weather Integration**: Real-time weather updates
- **Reminder System**: Voice-activated reminders
- **Multi-language Support**: Support for multiple languages

### Technical Improvements
- **Offline Mode**: Local speech recognition
- **Custom Wake Words**: User-defined activation phrases
- **Voice Training**: Personalized voice recognition
- **GUI Interface**: Graphical user interface
- **Mobile App**: Companion mobile application
- **Cloud Sync**: Settings and preferences sync

## Contributing

This project welcomes contributions in the following areas:
- **New Voice Commands**: Additional automation features
- **Music Library**: Expanding song collection
- **UI/UX**: Improving user experience
- **Documentation**: Enhancing guides and tutorials
- **Testing**: Comprehensive test coverage
- **Performance**: Optimization and efficiency improvements

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure API keys are properly configured
4. Test with the provided test scripts
5. Check microphone and audio settings

---

**Version**: 1.0  
**Last Updated**: 2025  
**Maintainer**: Python Project Collection  
**Status**: Fully Functional

## Acknowledgments

- **Google Speech Recognition**: For voice-to-text conversion
- **OpenAI**: For AI-powered responses
- **NewsAPI**: For news content
- **YouTube**: For music playback
- **gTTS**: For text-to-speech functionality
