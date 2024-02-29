# Programmer: Brian Kuhn
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")

import random

# Sample character database (name, type, price)
character_database = [
    {"name": "Peasant", "type": "Melee", "price": 10},
    {"name": "Footman", "type": "Melee", "price": 20},
    {"name": "Archer", "type": "Ranged", "price": 30},
    {"name": "Knight", "type": "Melee", "price": 50},
    {"name": "Catapult", "type": "Siege", "price": 100},
    # Add more characters as needed
]

import random
from collections import defaultdict

# Sample character database (name, type, price)
character_database = [
    {"name": "Peasant", "type": "Melee", "price": 10},
    {"name": "Footman", "type": "Melee", "price": 20},
    {"name": "Archer", "type": "Ranged", "price": 30},
    {"name": "Knight", "type": "Melee", "price": 50},
    {"name": "Catapult", "type": "Siege", "price": 100},
    # Add more characters as needed
]

def generate_random_army(max_price):
    army = []
    remaining_price = max_price

    while remaining_price > 0:
        unit = random.choice(character_database)
        if unit["price"] <= remaining_price:
            army.append(unit)
            remaining_price -= unit["price"]
        else:
            break

    return army

def count_characters(army):
    character_count = defaultdict(int)
    for unit in army:
        character_count[unit["name"]] += 1
    return character_count

def main():
    max_price = int(input("Enter the maximum price for the army: "))

    army = generate_random_army(max_price)

    print("\nRandomly Generated Army:")
    total_price = sum(unit["price"] for unit in army)
    print(f"Total Price: {total_price}")
    character_count = count_characters(army)
    print("Character Count:")
    for name, count in character_count.items():
        print(f"{name}: {count}")

if __name__ == "__main__":
    main()