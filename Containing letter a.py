list_1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Create a new list with items that contain the letter 'a'
new_list = []

for item in list_1:
    if "a" in item:
        new_list.append(item)

print(new_list)