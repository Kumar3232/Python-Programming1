correct_username = "python"
correct_password = "rules"

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    # Ask the user to enter username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the entered username and password are correct
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password.")
        attempts += 1

    if attempts == max_attempts:
        print("Access denied.")
