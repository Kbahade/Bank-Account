class BankAccount:
    def __init__(self, account_holder, password, balance=0):
        self.account_holder = account_holder
        self.password = password
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient balance for withdrawal."

    def check_balance(self, entered_password):
        if entered_password == self.password:
            return f"Account balance for {self.account_holder}: ${self.balance}"
        else:
            return "Incorrect password. Access denied."

def create_account():
    account_holder = input("Enter your name: ")
    password = input("Set your account password: ")
    return BankAccount(account_holder, password)

if __name__ == "__main__":
    accounts = {}

    print("Welcome to the Bank of Python")
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Already Have an Account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_account = create_account()
            accounts[new_account.account_holder] = new_account
            print(f"Account created for {new_account.account_holder}.")
        elif choice == "2":
            account_holder = input("Enter your name: ")
            if account_holder in accounts:
                account = accounts[account_holder]
                entered_password = input("Enter your account password: ")
                while True:
                    print("\nAccount Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Transaction History")
                    print("5. Back to Main Menu")

                    option = input("Enter your option: ")

                    if option == "1":
                        amount = float(input("Enter the deposit amount: $"))
                        print(account.deposit(amount))
                    elif option == "2":
                        amount = float(input("Enter the withdrawal amount: $"))
                        print(account.withdraw(amount))
                    elif option == "3":
                        print(account.check_balance(entered_password))
                    elif option == "4":
                        print("Transaction History:")
                        for transaction in account.transactions:
                            print(transaction)
                    elif option == "5":
                        break
                    else:
                        print("Invalid option. Please enter a valid choice.")
            else:
                print("Account not found. Please create an account first.")
        elif choice == "3":
            print("Thank you for using the Bank of Python. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
