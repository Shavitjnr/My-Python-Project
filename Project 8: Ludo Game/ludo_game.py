import random

# Assign colors
available_colors = ["Red", "Blue", "Green", "Yellow"]
target_position = 50

# Ask number of players
while True:
    num_players = int(input("Enter number of players (2-4): "))
    if 2 <= num_players <= 4:
        break
    print("Please enter a number between 2 and 4.")

# Setup players
players = []
for i in range(num_players):
    player_name = input(f"Enter name for Player {i + 1}: ")
    player_color = available_colors[i]
    players.append({"name": player_name, "color": player_color, "position": 0})

print("\n🎲 LUDO GAME STARTS! First to reach position", target_position, "wins!\n")

# Game loop
game_over = False
turn = 0

while not game_over:
    current_player = players[turn % num_players]
    input(f"{current_player['name']} ({current_player['color']}), press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print(f"🎲 {current_player['name']} rolled a {dice}!")

    current_player['position'] += dice
    if current_player['position'] >= target_position:
        print(f"🏆 {current_player['name']} ({current_player['color']}) wins the game!")
        game_over = True
    else:
        print(f"{current_player['name']}'s new position: {current_player['position']}\n")

    turn += 1
