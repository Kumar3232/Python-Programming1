# Ask the user for the number of the month
month = int(input("Enter the number of the month (1-12): "))

# Check the month and print the corresponding season
if month == 12 or month == 1 or month == 2:
    print("The season is Winter.")
elif month == 3 or month == 4 or month == 5:
    print("The season is Spring.")
elif month == 6 or month == 7 or month == 8:
    print("The season is Summer.")
elif month == 9 or month == 10 or month == 11:
    print("The season is Autumn.")
else:
    print("Invalid month! Please enter a number between 1 and 12.")
