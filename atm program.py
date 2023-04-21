print("Welcome to the ATM!")
pin = input("Please enter your 4-digit PIN: ")

if len(pin) == 4 and pin.isdigit():
    print("PIN verification successful.\n")

    while True:
        print("Please choose from the following options:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Print Mini Statement")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = input("Enter amount to withdraw: ")
            print(f"You have withdrawn {amount} .")
        elif choice == "2":
            amount = input("Enter amount to deposit: ")
            print(f"You have deposited {amount} .")
        elif choice == "3":
            balance = 10000.00  # Replace with actual account balance
            print(f"Your current balance is {balance} .")
        elif choice == "4":
            print("Mini statement:\n")
            # Print mini statement here
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

else:
    print("Invalid PIN. Please enter a 4-digit PIN.\n")```

#This version uses more descriptive variable names, proper indentation and spacing, and includes error handling to ensure the user inputs a valid 4-digit PIN. Additionally, it uses a `while True` loop to keep prompting the user until they choose to quit, and includes a "Quit" option in the menu.
