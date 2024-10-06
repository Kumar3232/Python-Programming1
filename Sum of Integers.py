def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def main():
    my_list = [23, 32, 12, 6, 54]

    result = sum_of_list(my_list)

    print(f"The sum of the list is: {result}")

main()
