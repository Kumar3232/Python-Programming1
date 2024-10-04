import random

def roll_dice(sides):
    return random.randint(1, sides)


# Main program
def main():
    # Ask the user for the number of sides on the dice
    sides = int(input("Enter the number of sides on the dice: "))
    dice_roll = 0

    # Keep rolling the dice until we get the maximum number
    while dice_roll != sides:
        dice_roll = roll_dice(sides)
        print(f"Rolled: {dice_roll}")

# Call the main function to start the program
main()
