inches = 0

while inches >= 0:
    # Ask the user to input the value in inches
    inches = float(input("Enter a value in inches (negative value to stop): "))

    if inches < 0:
        print("Program ended.")
        break

    # Convert inches to centimeters
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")
