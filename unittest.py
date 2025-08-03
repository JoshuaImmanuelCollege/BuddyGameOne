import unittest
from player import Player
from world import rooms

class TestPlayer(unittest.TestCase):
    def test_player_starts_in_room(self):
        player = Player("Tester", "entrance")
        self.assertEqual(player.current_room, "entrance")

    def test_inventory_starts_empty(self):
        player = Player("Tester", "entrance")
        self.assertEqual(player.inventory, [])

if __name__ == "__main__":
    unittest.main()

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

def main():
    player = Player("Adventurer", current_room="entrance")

    print("Welcome to the Dark Dungeon Escape!")
    print("Type 'help' to see commands.\n")

    while True:
        room = rooms[player.current_room]
        print(f"\nYou are in {room['name']}")
        print(room['description'])

        command = input("\nWhat do you do? ").strip().lower()

        if command == "help":
            print("Commands: go [direction], look, inventory, quit")
        elif command.startswith("go "):
            direction = command[3:]
            if direction in room['exits']:
                player.current_room = room['exits'][direction]
                print(f"You move {direction}.")
            else:
                print("You can't go that way.")
        elif command == "look":
            print(room['description'])
        elif command == "inventory":
            print("You have:", player.inventory or "nothing.")
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()

# rooms.py
rooms = {
    "entrance": {
        "name": "Dungeon Entrance",
        "description": "A dark, damp entrance to the dungeon. Paths lead north and east.",
        "exits": {"north": "hallway", "east": "armory"}
    },
    "hallway": {
        "name": "Long Hallway",
        "description": "A narrow corridor with flickering torches.",
        "exits": {"south": "entrance"}
    },
    "armory": {
        "name": "Old Armory",
        "description": "Broken weapons and armor are scattered around.",
        "exits": {"west": "entrance"}
    }
}
