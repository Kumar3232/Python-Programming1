# Size limit for a zander in centimeters
SIZE_LIMIT = 42

# Ask for the length of the zander
length = float(input("Enter the length of the zander (cm): "))

# Check if the zander meets the size limit
if length < SIZE_LIMIT:
    print(f"Release the fish! It is {SIZE_LIMIT - length} cm below the size limit.")
else:
    print("You can keep the fish.")
