def remove_odd_numbers(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list


# Main program
def main():

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Original list:", original_list)

    even_list = remove_odd_numbers(original_list)

    print("List with odd numbers removed:", even_list)

main()
