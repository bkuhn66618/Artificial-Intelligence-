# Programmer: Brian Kuhn
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")
"""
import random

# Define a function to generate a random password
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(){}[]_+?-=`~"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

# Main function
def main():
    # Get user input for password length
    length = int(input("Enter the length of the password: "))

    # Generate and print the password
    password = generate_password(length)
    print("Generated password:", password)

# Call the main function
if __name__ == "__main__":
    main()
"""
import random

# Define the player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def attack(self):
        dice_size = int(input("Enter the size of the dice to roll (e.g., 4, 6, 8, 10, 12, 20): "))
        roll = random.randint(1, dice_size)
        print("You rolled 1d{} for {} damage.".format(dice_size, roll))
        return roll

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health = min(100, self.health + amount)

    def is_alive(self):
        return self.health > 0

# Define the Room class
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enemies = []
        self.treasures = []
        self.explored = False

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_treasure(self, treasure):
        self.treasures.append(treasure)

    def explore(self, player):
        if not self.explored:
            self.explored = True
            print("You explore the room and find:")
            for treasure in self.treasures:
                print("- {} worth {} gold coins".format(treasure.name, treasure.value))
                player.inventory.append(treasure)
                if treasure.name == "Health Potion":
                    player.heal(treasure.value)
                    print("- You found a health potion and healed for {} HP!".format(treasure.value))
            for enemy in self.enemies:
                print("- A {}".format(enemy.name))
            if random.random() < 0.1:  # 10% chance of encountering an additional enemy
                print("- You sense a presence...")
                self.add_enemy(Enemy("Dragon", 150, 25))

# Define the Enemy class
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self):
        dice_size = 20
        roll = random.randint(1, dice_size)
        print("The {} rolled 1d{} for {} damage.".format(self.name, dice_size, roll))
        return roll

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

# Define the Treasure class
class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Main function
def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    # Create rooms
    room1 = Room("Room 1", "You are in a dark room.")
    room2 = Room("Room 2", "You are in a spooky corridor.")
    room3 = Room("Room 3", "You are in a mysterious chamber.")
    room4 = Room("Room 4", "You are in a narrow passage.")
    room5 = Room("Room 5", "You are in a brightly lit hall.")

    # Add enemies and treasures to rooms
    room1.add_enemy(Enemy("Goblin", 30, 10))
    room1.add_treasure(Treasure("Gold Coin", 20))
    room2.add_enemy(Enemy("Skeleton", 40, 15))
    room2.add_treasure(Treasure("Silver Sword", 50))
    room3.add_enemy(Enemy("Zombie", 50, 20))
    room3.add_treasure(Treasure("Health Potion", 30))
    room4.add_enemy(Enemy("Witch", 60, 25))
    room4.add_treasure(Treasure("Ruby Gem", 100))
    room5.add_enemy(Enemy("Orc", 70, 30))
    room5.add_treasure(Treasure("Diamond", 150))

    rooms = [room1, room2, room3, room4, room5]
    current_room = random.choice(rooms)

    # Game loop
    while True:
        print("\n" + current_room.name)
        print("Player Health: {}".format(player.health))
        print(current_room.description)

        # Check for enemies
        for enemy in current_room.enemies:
            print("A {} appears!".format(enemy.name))

            # Battle loop
            while player.is_alive() and enemy.is_alive():
                player_damage = player.attack()
                enemy_damage = enemy.attack()

                print("You attack the {} for {} damage.".format(enemy.name, player_damage))
                enemy.take_damage(player_damage)

                if enemy.is_alive():
                    print("The {} attacks you for {} damage.".format(enemy.name, enemy_damage))
                    if enemy_damage == 20:
                        print("The {} missed!".format(enemy.name))
                    else:
                        player.take_damage(enemy_damage)

                    if player.is_alive():
                        print("You defeated the {}!".format(enemy.name))
                        current_room.enemies.remove(enemy)
                    else:
                        print("You were defeated by the {}!".format(enemy.name))
                        break
                else:
                    print("Game Over! You died.")
                    return

            # Explore the room
            if not player.is_alive():
                print("Game Over! You died.")
                break

            action = input("What would you like to do? (explore/move/quit): ")

            if action == "quit":
                print("Thanks for playing!")
                break
            elif action == "explore":
                current_room.explore(player)
            elif action == "move":
                next_room = current_room
                while next_room == current_room:
                    next_room = random.choice(rooms)
                    if next_room == current_room:
                        # Check if there should be a new enemy
                        if random.random() < 0.25:  # 25% chance of encountering a new enemy
                            enemy = Enemy("New Enemy", random.randint(20, 40), random.randint(5, 15))
                            next_room.add_enemy(enemy)
                            print("A new enemy, {}, appears in the {}!".format(enemy.name, next_room.name))

                        # Check if there should be a new treasure
                        if random.random() < 0.5:  # 50% chance of finding a new treasure
                            treasure_name = random.choice(["Health Potion", "Gold Coin", "Ruby Gem"])
                            treasure_value = random.randint(10, 100)
                            treasure = Treasure(treasure_name, treasure_value)
                            next_room.add_treasure(treasure)
                            print("You found a {} worth {} gold coins in the {}!".format(treasure_name, treasure_value,
                                                                                         next_room.name))

                print("You move to the {}.".format(next_room.name))
                current_room = next_room
            else:
                print("Invalid action. Please choose explore, move, or quit.")

    # Call the main function
    if __name__ == "__main__":
        main()
