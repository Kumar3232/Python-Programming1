import random

# Ask the user how many dice to roll
num_dice = int(input("How many dice would you like to roll? "))

# Initialize a variable to hold the sum of the dice rolls
total_sum = 0

# Roll each die and add the result to the total sum
for _ in range(num_dice):
    roll = random.randint(1, 6)  # Randomly choose a number between 1 and 6
    total_sum += roll

# Print the total sum of the dice rolls
print(f"The sum of your {num_dice} dice rolls is: {total_sum}")
