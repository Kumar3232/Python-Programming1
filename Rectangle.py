# Ask the user for input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Calculate the perimeter of the rectangle
perimeter = 2 * (length + width)

# Print out the area and perimeter of the rectangle
print(f"The area of the rectangle is {area:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")
