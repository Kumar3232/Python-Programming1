# Function to write new notes to a file
def write_notes():
    with open("notes.txt", "w") as file:
        note = input("Enter your note: ")
        file.write(note + "\n")
    print("Note written to file.")

# Function to read existing notes from the file
def read_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("Existing notes:")
                for note in notes:
                    print(note.strip())
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found. You can start writing new notes.")

# Function to append additional notes to the file
def append_notes():
    with open("notes.txt", "a") as file:
        note = input("Enter your additional note: ")
        file.write(note + "\n")
    print("Additional note appended to file.")

# Main menu to choose options
def main():
    while True:
        print("\nOptions:")
        print("1. Write new notes (this will overwrite existing notes).")
        print("2. Read existing notes.")
        print("3. Append additional notes.")
        print("4. Exit.")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            write_notes()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            append_notes()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
