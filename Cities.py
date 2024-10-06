cities = []

# Use a for loop to ask the user to enter the names of five cities
for i in range(5):
    city = input(f"Enter the name of city #{i+1}: ")
    cities.append(city)  # Add each city to the list

# Print out the names of the cities one by one using a for/in loop
print("\nThe cities you entered are:")
for city in cities:
    print(city)
