# Create an empty list to store the names
names = []

# Continuously prompt the user for names
while True:
    name = input("Enter a name (or press Enter to finish): ")

    if name == "":  # Stop when the user enters an empty string
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.append(name)  # Add the new name to the list

# Print out the names one by one
print("\nThe names you entered are:")
for name in names:
    print(name)
