import musicLibrary

def test_song_playing():
    print("Testing song playing functionality...")
    print("\nAvailable songs in library:")
    for i, song in enumerate(musicLibrary.music.keys(), 1):
        print(f"{i}. {song}")
    
    print("\nTesting song search:")
    # Test all songs in the library
    test_commands = [
        "play skyfall",
        "play moonlight", 
        "play 11k",
        "play raat rani",
        "play sad ganna",
        "play jhol",
        "play with you",
        "play let the world burn",
        "play zara zara",
        "play make the angels cry",
        "play unknown song"
    ]
    
    for command in test_commands:
        print(f"\nCommand: '{command}'")
        song_name = command.lower().replace("play", "").strip()
        
        song_found = False
        for song_key, song_url in musicLibrary.music.items():
            if song_name in song_key.lower() or song_key.lower() in song_name:
                print(f"✓ Found: {song_key}")
                print(f"  URL: {song_url}")
                song_found = True
                break
        
        if not song_found:
            print(f"✗ Not found: '{song_name}'")
    
    print(f"\nTotal songs in library: {len(musicLibrary.music)}")

if __name__ == "__main__":
    test_song_playing() 