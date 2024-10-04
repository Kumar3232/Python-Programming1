import math

# Function to calculate the unit price of a pizza
def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2) / 10000  # Convert area to square meters
    return price / area

# Main program
def main():
    # Pizza 1 input
    d1 = float(input("Enter the diameter of the first pizza (in cm): "))
    p1 = float(input("Enter the price of the first pizza (in euros): "))

    # Pizza 2 input
    d2 = float(input("Enter the diameter of the second pizza (in cm): "))
    p2 = float(input("Enter the price of the second pizza (in euros): "))

    # Calculate unit prices
    price1 = unit_price(d1, p1)
    price2 = unit_price(d2, p2)

    # Compare and print the better value
    if price1 < price2:
        print("The first pizza is better value for money.")
    elif price2 < price1:
        print("The second pizza is better value for money.")
    else:
        print("Both pizzas offer the same value.")

main()
