# Function to ask the user for account balance and withdrawal amount
def main():
    try:
        # Get the account balance from the user
        balance = float(input("Enter your account balance: "))
        if balance < 0:
            raise ValueError("Account balance cannot be negative.")

        # Get the withdrawal amount from the user
        withdrawal = float(input("Enter the withdrawal amount: "))
        if withdrawal < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if withdrawal > balance:
            raise ValueError("Withdrawal amount exceeds the balance.")

        # If everything is fine, print the new balance after withdrawal
        new_balance = balance - withdrawal
        print(f"Withdrawal successful. Your new balance is: {new_balance:.2f}.")

    # Handle cases where the input is not a number
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
