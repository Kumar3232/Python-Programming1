import random

# Generate a 3-digit code (each number between 0 and 9)
code_3_digit = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

# Generate a 4-digit code (each number between 1 and 6)
code_4_digit = f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"

# Print the generated codes
print(f"3-digit code: {code_3_digit}")
print(f"4-digit code: {code_4_digit}")