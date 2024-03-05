# Programmer: Brian Kuhn
# Date: 2.29.2024
# Program: AI Playground

print("This will be a place for me to play with programming using AI Technology\n")

import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides for your dice: "))
    if sides <= 0:
        print("Invalid number of sides. Please enter a positive integer.")
        return
    roll = roll_dice(sides)
    print("You rolled:", roll)

if __name__ == "__main__":
    main()
