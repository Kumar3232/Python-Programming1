# Conversion constants
LOT_TO_GRAMS = 13.3
POUND_TO_GRAMS = 32 * LOT_TO_GRAMS
TALENT_TO_GRAMS = 20 * POUND_TO_GRAMS

# Ask the user for input in talents, pounds, and lots
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Convert everything to grams
total_grams = (talents * TALENT_TO_GRAMS) + (pounds * POUND_TO_GRAMS) + (lots * LOT_TO_GRAMS)

# Convert grams to kilograms and grams
kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

# Output the result
print(f"The weight in modern units: {kilograms} kilograms and {remaining_grams:.2f} grams.")
