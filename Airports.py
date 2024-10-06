# Create an empty dictionary to store airport data
airport_data = {}

while True:
    # Display options to the user
    print("\n1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    # Get the user's choice
    choice = input("Choose an option (1, 2, or 3): ")

    if choice == "1":
        # Add a new airport
        icao_code = input("Enter the ICAO code: ").upper()
        name = input("Enter the name of the airport: ")
        airport_data[icao_code] = name
        print("Airport added.")

    elif choice == "2":
        # Get information about an existing airport
        icao_code = input("Enter the ICAO code to find: ").upper()
        if icao_code in airport_data:
            print(f"Airport name: {airport_data[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == "3":
        # Quit the program
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
