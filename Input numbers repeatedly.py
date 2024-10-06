# Initialize an empty list to store the numbers
numbers = []

# Continuously prompt the user for numbers
while True:
    user_input = input("Enter a number (or press Enter to finish): ")

    if user_input == "":  # Stop when the user enters an empty string
        break

    # Convert the input to a number and add it to the list
    try:
        number = float(user_input)  # Using float to handle both integers and decimal numbers
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Sort the list in descending order
numbers.sort(reverse=True)

# Get the five greatest numbers (or fewer if there are less than 5)
top_five = numbers[:5]

# Print the result
print(f"The five greatest numbers are: {top_five}")
