import random

def roll_dice():
    return random.randint(1,6)

#Main program
def main():
    dice_roll = 0

    while dice_roll != 6:
        dice_roll = roll_dice()
        print(f"Rolled: {dice_roll}")

main()