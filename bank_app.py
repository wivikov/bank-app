from BankApp.bank_db import BankDatabase
from datetime import datetime

class BankApp:
    def __init__(self):
        self.db = BankDatabase()
        self.users = self.db.load_users()
        self.current_user = None

    def log_transaction(self, message):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        with open("transactions.log", "a") as log_file:
            log_file.write(f"{timestamp} {message}\n")

    def register_user(self):
        username = input("Enter username: ").lower()
        if username in self.users:
            print("User already exists")
            return
        email = input("Enter email: ")
        balance = 0
        self.users[username] = {
            "email": email,
            "balance": balance
        }
        self.db.save_users(self.users)
        print(f"User '{username}' registered successfully!")

    def login_user(self):
        username = input("Enter username: ").lower()
        if username not in self.users:
            print("User not found")
            return
        self.current_user = username
        print(f"Welcome, {username}!")
        self.user_menu()

    def user_menu(self):
        while True:
            print("\n--- User Menu ---")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")

            choice = input("Choose option: ")
            if choice == "1":
                print("Balance:", self.users[self.current_user]["balance"])
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                if amount > 0:
                    self.users[self.current_user]["balance"] += amount
                    self.db.save_users(self.users)
                    print("Deposit successful")
                    self.log_transaction(f"User '{self.current_user}' deposited {amount}")
                else:
                    print("Invalid deposit amount")
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                elif amount > self.users[self.current_user]["balance"]:
                    print("Not enough funds")
                else:
                    self.users[self.current_user]["balance"] -= amount
                    self.db.save_users(self.users)
                    print("Withdraw successful")
                    self.log_transaction(f"User '{self.current_user}' withdrew {amount}")
            elif choice == "4":
                self.db.save_users(self.users)
                self.log_transaction(f"User '{self.current_user}' logged out")
                print(f"Goodbye, {self.current_user}")
                self.current_user = None
                break
            else:
                print("Invalid option")


# Запуск програми:
if __name__ == "__main__":
    app = BankApp()
    while True:
        print("\n=== Welcome to Python Bank ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            app.register_user()
        elif choice == "2":
            app.login_user()
        elif choice == "3":
            print("Thanks for using our bank!")
            break
        else:
            print("Invalid input. Try again.")