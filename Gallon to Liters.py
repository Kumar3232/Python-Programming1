def gallons_to_liters(gallons):
    return gallons * 3.78541  # 1 gallon = 3.78541 liters

def main():
    while True:
        # Ask the user for the volume in gallons
        gallons = float(input("Enter the volume in gallons (negative to quit): "))

        # Check if the input is negative to exit the loop
        if gallons < 0:
            print("Exiting the program.")
            break

        # Convert gallons to liters using the function
        liters = gallons_to_liters(gallons)

        # Print the converted value
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")

# Call the main function to start the program
main()
