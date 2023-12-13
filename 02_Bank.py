class BankAccount:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

# Example usage:
account_number = input("Enter account number: ")
name = input("Enter account holder's name: ")

# Display account type options
print("Select account type:")
print("1. Savings")
print("2. Current")
print("3. Business")

choice = input("Enter your choice (1/2/3): ")

account_type_options = {"1": "Savings", "2": "Current", "3": "Business"}
selected_account_type = account_type_options.get(choice, "Invalid Choice")

initial_balance = float(input("Enter initial balance: "))

# Create a BankAccount object
bank_account = BankAccount(account_number, name, selected_account_type, initial_balance)

# Menu-driven options for deposit, withdrawal, checking balance, or exiting
while True:
    print("\nSelect operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    operation_choice = input("Enter your choice (1/2/3/4): ")

    if operation_choice == "1":
        deposit_amount = float(input("Enter deposit amount: "))
        bank_account.deposit(deposit_amount)
    elif operation_choice == "2":
        withdraw_amount = float(input("Enter withdrawal amount: "))
        bank_account.withdraw(withdraw_amount)
    elif operation_choice == "3":
        bank_account.check_balance()
    elif operation_choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
