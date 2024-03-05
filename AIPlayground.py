# Programmer: Brian Kuhn
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")

import random
import time
from collections import defaultdict

# Sample character database (name, type, price, group)
character_database = [
    # Baseline for the characters
    # {"name": "", "type": "", "price": , "group": ""},
    {"name": "Clubber", "type": "Melee", "price": 70, "group": "Tribal"},
    {"name": "Protector", "type": "Melee", "price": 80, "group": "Tribal"},
    {"name": "Spear Thrower", "type": "Ranged", "price": 120, "group": "Tribal"},
    {"name": "Stoner", "type": "Ranged", "price": 160, "group": "Tribal"},
    {"name": "Bone Mage", "type": "Ranged", "price": 300, "group": "Tribal"},
    {"name": "Chieftain", "type": "Melee", "price": 400, "group": "Tribal"},
    {"name": "Mammoth", "type": "Melee", "price": 2200, "group": "Tribal"},
    {"name": "Halfling", "type": "Melee", "price": 50, "group": "Farmer"},
    {"name": "Farmer", "type": "Melee", "price": 80, "group": "Farmer"},
    {"name": "Hay Baler", "type": "Melee", "price": 140, "group": "Farmer"},
    {"name": "Potionseller", "type": "Ranged", "price": 340, "group": "Farmer"},
    {"name": "Harvester", "type": "Melee", "price": 500, "group": "Farmer"},
    {"name": "Wheelbarrow", "type": "Melee", "price": 1000, "group": "Farmer"},
    {"name": "Scarecrow", "type": "Ranged", "price": 1200, "group": "Farmer"},
    {"name": "Bard", "type": "None", "price": 60, "group": "Medieval"},
    {"name": "Squire", "type": "Melee", "price": 100, "group": "Medieval"},
    {"name": "Archer", "type": "Ranged", "price": 140, "group": "Medieval"},
    {"name": "Healer", "type": "Ranged", "price": 180, "group": "Medieval"},
    {"name": "Knight", "type": "Melee", "price": 650, "group": "Medieval"},
    {"name": "Catapult", "type": "Ranged", "price": 1000, "group": "Medieval"},
    {"name": "The King", "type": "Melee", "price": 1500, "group": "Medieval"},
    {"name": "Shield Bearer", "type": "Melee", "price": 100, "group": "Ancient"},
    {"name": "Sarissa", "type": "Melee", "price": 120, "group": "Ancient"},
    {"name": "Hoplite", "type": "Melee", "price": 180, "group": "Ancient"},
    {"name": "Snake Archer", "type": "Ranged", "price": 300, "group": "Ancient"},
    {"name": "Ballista", "type": "Ranged", "price": 900, "group": "Ancient"},
    {"name": "Minotaur", "type": "Melee", "price": 1600, "group": "Ancient"},
    {"name": "Zues", "type": "Ranged", "price": 2000, "group": "Ancient"},
    {"name": "Headbutter", "type": "Melee", "price": 90, "group": "Viking"},
    {"name": "Ice Archer", "type": "Ranged", "price": 160, "group": "Viking"},
    {"name": "Brawler", "type": "Melee", "price": 220, "group": "Viking"},
    {"name": "Berserker", "type": "Melee", "price": 250, "group": "Viking"},
    {"name": "Valkyrie", "type": "Melee", "price": 500, "group": "Viking"},
    {"name": "Longship", "type": "Melee", "price": 1000, "group": "Viking"},
    {"name": "Jarl", "type": "Melee", "price": 1500, "group": "Viking"},
    {"name": "Samurai", "type": "Melee", "price": 140, "group": "Dynasty"},
    {"name": "Firework Archer", "type": "Ranged", "price": 180, "group": "Dynasty"},
    {"name": "Monk", "type": "Melee", "price": 250, "group": "Dynasty"},
    {"name": "Ninja", "type": "Ranged", "price": 500, "group": "Dynasty"},
    {"name": "Dragon", "type": "Ranged", "price": 1000, "group": "Dynasty"},
    {"name": "Hwacha", "type": "Ranged", "price": 1500, "group": "Dynasty"},
    {"name": "Monkey King", "type": "Melee", "price": 2000, "group": "Dynasty"},
    {"name": "Painter", "type": "Melee", "price": 50, "group": "Renaissance"},
    {"name": "Fencer", "type": "Melee", "price": 150, "group": "Renaissance"},
    {"name": "Balloon Archer", "type": "Ranged", "price": 200, "group": "Renaissance"},
    {"name": "Muskateer", "type": "Ranged", "price": 250, "group": "Renaissance"},
    {"name": "Halberd", "type": "Melee", "price": 400, "group": "Renaissance"},
    {"name": "Jouster", "type": "Melee", "price": 1000, "group": "Renaissance"},
    {"name": "Da Vanci Tank", "type": "Ranged", "price": 4000, "group": "Renaissance"},
    {"name": "Flintlock", "type": "Ranged", "price": 100, "group": "Pirate"},
    {"name": "Blunderbuss", "type": "Ranged", "price": 160, "group": "Pirate"},
    {"name": "Bomb Thrower", "type": "Ranged", "price": 250, "group": "Pirate"},
    {"name": "Harpooner", "type": "Ranged", "price": 300, "group": "Pirate"},
    {"name": "Cannon", "type": "Ranged", "price": 1000, "group": "Pirate"},
    {"name": "Captain", "type": "Ranged", "price": 1500, "group": "Pirate"},
    {"name": "Pirate Queen", "type": "Melee", "price": 2500, "group": "Pirate"},
    {"name": "Skeleton Warrior", "type": "Melee", "price": 80, "group": "Spooky"},
    {"name": "Swordcaster", "type": "Ranged", "price": 1000, "group": "Spooky"},
    {"name": "Vampires", "type": "Melee", "price": 200, "group": "Spooky"},
    {"name": "Skeleton Archer", "type": "Ranged", "price": 180, "group": "Spooky"},
    {"name": "Candlehead", "type": "Ranged", "price": 200, "group": "Spooky"},
    {"name": "Pumpkin Catapult", "type": "Ranged", "price": 1000, "group": "Spooky"},
    {"name": "Reaper", "type": "Melee", "price": 2500, "group": "Spooky"},
    {"name": "Dynamite Thrower", "type": "Ranged", "price": 100, "group": "Wild West"},
    {"name": "Miner", "type": "Melee", "price": 200, "group": "Wild West"},
    {"name": "Cactus", "type": "Melee", "price": 400, "group": "Wild West"},
    {"name": "Gunslinger", "type": "Ranged", "price": 650, "group": "Wild West"},
    {"name": "Lasso", "type": "Ranged", "price": 740, "group": "Wild West"},
    {"name": "Deadeye", "type": "Ranged", "price": 900, "group": "Wild West"},
    {"name": "Quick Draw", "type": "Ranged", "price": 1200, "group": "Wild West"},
    {"name": "Peasant", "type": "Melee", "price": 30, "group": "Legacy"},
    {"name": "Banner Bearer", "type": "Melee", "price": 100, "group": "Legacy"},
    {"name": "Peasant", "type": "Melee", "price": 30, "group": "Legacy"},
    {"name": "Poacher", "type": "Ranged", "price": 120, "group": "Legacy"},
    {"name": "Blowdarter", "type": "Ranged", "price": 220, "group": "Legacy"},
    {"name": "Pike", "type": "Melee", "price": 300, "group": "Legacy"},
    {"name": "Barrel Roller", "type": "Melee", "price": 350, "group": "Legacy"},
    {"name": "Boxer", "type": "Melee", "price": 450, "group": "Legacy"},
    {"name": "Flag Bearer", "type": "Melee", "price": 500, "group": "Legacy"},
    {"name": "Pharaoh", "type": "Melee", "price": 750, "group": "Legacy"},
    {"name": "Wizard", "type": "Ranged", "price": 1200, "group": "Legacy"},
    {"name": "Chariot", "type": "Melee", "price": 1800, "group": "Legacy"},
    {"name": "Thor", "type": "Melee", "price": 2200, "group": "Legacy"},
    {"name": "Tank", "type": "Ranged", "price": 6000, "group": "Legacy"},
    {"name": "Super Boxer", "type": "Melee", "price": 10000, "group": "Legacy"},
    {"name": "Dark Peasant", "type": "Melee", "price": 9999999, "group": "Legacy"},
    {"name": "Super Peasant", "type": "Melee", "price": 9999999, "group": "Legacy"},
    {"name": "Devout Gauntlet", "type": "Melee", "price": 200, "group": "Good"},
    {"name": "Celestial Aegis", "type": "Ranged", "price": 300, "group": "Good"},
    {"name": "Radient Glaive", "type": "Melee", "price": 500, "group": "Good"},
    {"name": "Righteous Paladin", "type": "Melee", "price": 800, "group": "Good"},
    {"name": "Divine Arbiter", "type": "Ranged", "price": 1000, "group": "Good"},
    {"name": "Sacred Elephant", "type": "Melee", "price": 2000, "group": "Good"},
    {"name": "Chronomancer", "type": "Ranged", "price": 3000, "group": "Good"},
    {"name": "Shadow Walker", "type": "Melee", "price": 200, "group": "Evil"},
    {"name": "Exiled Sentinel", "type": "Melee", "price": 300, "group": "Evil"},
    {"name": "Mad Mechanic", "type": "Ranged", "price": 500, "group": "Evil"},
    {"name": "Void Cyltist", "type": "Ranged", "price": 800, "group": "Evil"},
    {"name": "Tempest Lich", "type": "Ranged", "price": 1000, "group": "Evil"},
    {"name": "Death Bringer", "type": "Melee", "price": 2000, "group": "Evil"},
    {"name": "Void Monarch", "type": "Melee", "price": 3000, "group": "Evil"},
    {"name": "Ballooner", "type": "Ranged", "price": 120, "group": "Secret"},
    {"name": "Bomb On A Stick", "type": "Melee", "price": 150, "group": "Secret"},
    {"name": "Fan Bearer", "type": "Ranged", "price": 200, "group": "Secret"},
    {"name": "Raptor", "type": "Melee", "price": 200, "group": "Secret"},
    {"name": "The Teacher", "type": "Melee", "price": 200, "group": "Secret"},
    {"name": "Jester", "type": "Melee", "price": 300, "group": "Secret"},
    {"name": "Ball 'n' Chain", "type": "Ranged", "price": 350, "group": "Secret"},
    {"name": "Chu Ko Nu", "type": "Ranged", "price": 350, "group": "Secret"},
    {"name": "Executioner", "type": "Melee", "price": 350, "group": "Secret"},
    {"name": "Shouter", "type": "Ranged", "price": 400, "group": "Secret"},
    {"name": "Taekwondo", "type": "Melee", "price": 400, "group": "Secret"},
    {"name": "Raptor Rider", "type": "Melee", "price": 450, "group": "Secret"},
    {"name": "Cheerleader", "type": "None", "price": 500, "group": "Secret"},
    {"name": "Cupid", "type": "Ranged", "price": 500, "group": "Secret"},
    {"name": "Mace Spinner", "type": "Melee", "price": 500, "group": "Secret"},
    {"name": "CLAMS", "type": "Ranged", "price": 500, "group": "Secret"},
    {"name": "Present Elf", "type": "Ranged", "price": 500, "group": "Secret"},
    {"name": "Ice Mage", "type": "Ranged", "price": 650, "group": "Secret"},
    {"name": "Infernal Whip", "type": "Ranged", "price": 800, "group": "Secret"},
    {"name": "Bank Robbers", "type": "Ranged", "price": 850, "group": "Secret"},
    {"name": "Witch", "type": "Ranged", "price": 1000, "group": "Secret"},
    {"name": "Banshee", "type": "Ranged", "price": 1100, "group": "Secret"},
    {"name": "Necromancer", "type": "Ranged", "price": 1200, "group": "Secret"},
    {"name": "Solar Architect", "type": "Ranged", "price": 1200, "group": "Secret"},
    {"name": "Wheelbarrow Dragon", "type": "Ranged", "price": 1400, "group": "Secret"},
    {"name": "Bomb Cannon", "type": "Ranged", "price": 1500, "group": "Secret"},
    {"name": "Skeleton Giant", "type": "Melee", "price": 1700, "group": "Secret"},
    {"name": "Cavalry", "type": "Melee", "price": 1800, "group": "Secret"},
    {"name": "Vlad", "type": "Melee", "price": 1800, "group": "Secret"},
    {"name": "Gatling Gun", "type": "Ranged", "price": 2000, "group": "Secret"},
    {"name": "Blackbeard", "type": "Melee", "price": 2600, "group": "Secret"},
    {"name": "Samurai Giant", "type": "Melee", "price": 3000, "group": "Secret"},
    {"name": "Ullr", "type": "Melee", "price": 3000, "group": "Secret"},
    {"name": "Lady Red Jade", "type": "Melee", "price": 3500, "group": "Secret"},
    {"name": "Sensei", "type": "Ranged", "price": 3500, "group": "Secret"},
    {"name": "Shogun", "type": "Melee", "price": 3500, "group": "Secret"},
    {"name": "Tree Giant", "type": "Melee", "price": 4000, "group": "Secret"},
    {"name": "Artemis", "type": "Ranged", "price": 5500, "group": "Secret"},
    {"name": "Ice Giant", "type": "Melee", "price": 6000, "group": "Secret"},
]


def generate_random_army(max_price, max_unique_units, max_units_per_type=None, group=None):
    group_input = group
    if group_input:
        available_characters = [char for char in character_database if char["group"] in group_input]
    else:
        available_characters = character_database

    if not available_characters:
        print("No characters available based on the specified group(s).")
        return []

    army = []
    remaining_price = max_price
    unique_units_generated = set()
    unique_types_added = 0

    random.shuffle(available_characters)  # Shuffle the list of available characters

    for char in available_characters:
        if remaining_price <= 0 or unique_types_added >= max_unique_units:
            break

        if char["name"] not in unique_units_generated and char["price"] <= remaining_price:
            max_units = remaining_price // char["price"]
            if max_units_per_type is not None:
                max_units = min(max_units, max_units_per_type)
            if max_units == 0:
                continue
            num_units = random.randint(1, max_units)  # Randomly select the quantity of units
            army.extend([char] * num_units)
            remaining_price -= char["price"] * num_units
            unique_units_generated.add(char["name"])
            unique_types_added += 1

    # Add halflings and peasants if necessary
    while remaining_price > 0:
        fill_in_units = [char for char in available_characters if
                         char["price"] <= remaining_price and char["name"] in ("Halfling", "Peasant")]
        if not fill_in_units:
            break
        selected_unit = random.choice(fill_in_units)
        army.append(selected_unit)
        remaining_price -= selected_unit["price"]

    return army


def count_characters(army):
    character_count = defaultdict(int)
    for unit in army:
        character_count[unit["name"]] += 1
    return character_count


def main():
    max_price = int(input("Enter the maximum price for the army: "))
    num_unique_units = int(input("Enter the number of unique units for the army: "))
    max_units_per_type_input = input("Enter the maximum number of units for each type (press Enter for default): ")
    max_units_per_type = int(max_units_per_type_input) if max_units_per_type_input else None
    print(
        "Groups available: Ancient, Dynasty, Evil, Farmer, Good, Legacy, Medieval, Pirate, Renaissance, Secret, Spooky, Tribal, Viking, and Wild West\n")
    groups = []
    while True:
        group_input = input("Enter a faction to randomize from (or press Enter to finish): ").strip().capitalize()
        if not group_input:
            break
        groups.append(group_input)

    if not groups:
        group = None
    else:
        group = [group.capitalize() for group in groups]

    print("Generating army...", end="", flush=True)
    start_time = time.time()

    army = generate_random_army(max_price, num_unique_units, max_units_per_type, group)

    end_time = time.time()
    print("\n")
    print(f"Time taken: {end_time - start_time:.4f} seconds\n")

    print("Randomly Generated Army:")
    total_price = sum(unit["price"] for unit in army)
    left_over = max_price - total_price
    print(f"Money Spent: {total_price}")
    print(f"Money Left over: {left_over}")
    character_count = count_characters(army)

    characters_with_group = defaultdict(set)
    for unit in army:
        characters_with_group[unit['name']].add(unit['group'])

    sorted_characters = sorted(characters_with_group.items(), key=lambda x: x[0])

    print("Units:")
    total_cost = 0  # Initialize the total cost variable
    for name, groups in sorted_characters:
        group_str = ", ".join(groups)
        count = character_count[name]
        unit_price = [unit["price"] for unit in army if unit["name"] == name][0]
        total_cost += unit_price * count  # Update total cost
        print(f"{name} ({group_str}): {count} - Cost: {unit_price * count}")

    print("\nTotal Cost of Units:", total_cost)  # Print the total cost


if __name__ == "__main__":
    main()
    #print("\ngroups = Ancient, Dynasty, Evil, Farmer, Good, Legacy, Medieval, Pirate, Renaissance, Secret, Spooky, Tribal, Viking, and Wild West\n")