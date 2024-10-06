# Function to check if a number is prime
def is_prime(num):
    # Check if the number is less than 2 (not prime)
    if num < 2:
        return False
    # Check divisibility from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # If divisible by any number, it's not prime
    return True


# Ask the user for an integer input
try:
    number = int(input("Enter an integer: "))

    # Check if the number is prime and print the result
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
