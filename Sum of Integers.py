def sum_of_list(numbers):
    total = 0 # Initialize total to 0

    for number in numbers:

        total += number # Add each number to the total
    return total # Return the total sum

def main(): # Create a list of integers

    my_list = [23, 32, 12, 6, 54]

    result = sum_of_list(my_list)

    print(f"The sum of the list is: {result}")

# Call the main function to start the program
main()