def have_common_member(list1, list2):

    for item in list1:

        if item in list2:
            return True

    return False

list_a = [1, 2, 3, 4]
list_b = [4, 5, 6]

print(have_common_member(list_a, list_b))
