import math

def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)  #
    area_in_square_meters = area / 10000

    unit_price = price / area_in_square_meters

    return unit_price


def main():
    diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))

    diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))

    price2 = float(input("Enter the price of the second pizza (in euros): "))

    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    # Print out unit prices
    print(f"First pizza's unit price: {unit_price1:.2f} euros per square meter")
    print(f"Second pizza's unit price: {unit_price2:.2f} euros per square meter")

    # Compare unit prices and print which pizza is a better value
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas offer the same value for money.")

main()
