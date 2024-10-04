numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")
        continue

# Check if the list is not empty
if numbers:
    # Print the smallest and largest numbers
    print(f"The smallest number is: {min(numbers)}")
    print(f"The largest number is: {max(numbers)}")
else:
    print("No numbers were entered.")
