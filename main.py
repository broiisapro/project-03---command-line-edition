import os
import json
from datetime import datetime

class BudgetTracker:
    def __init__(self):
        # Initialize the tracker with some default values
        self.transactions = []
        self.categories = ['Food', 'Rent', 'Entertainment', 'Utilities', 'Transportation', 'Miscellaneous']
        self.file_name = 'transactions.json'
        self.load_transactions()
    
    def load_transactions(self):
        """Load transaction data from the file if it exists."""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                self.transactions = [Transaction(**item) for item in data]
        else:
            print("No previous transaction data found. Starting fresh.")
    
    def save_transactions(self):
        """Save transaction data to a file"""
        with open(self.file_name, 'w') as file:
            json.dump([transaction.to_dict() for transaction in self.transactions], file)
    
    def add_transaction(self, amount, category, description, date=None):
        """Add a transaction to the tracker"""
        if category not in self.categories:
            print("Invalid category, please choose from the following:", self.categories)
            return
        if not date:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fixed the date format
        transaction = Transaction(amount, category, description, date)
        self.transactions.append(transaction)
        print(f"Transaction added: {transaction}")
        self.save_transactions()

    def view_summary(self):
        """View the summary of all transactions"""
        print("\nSummary of Transactions\n")
        for category in self.categories:
            total = self.get_total_by_category(category)
            print(f"{category}: {total}")
    
    def get_total_by_category(self, category):
        """Get the total spending for a specific category."""
        return sum(t.amount for t in self.transactions if t.category == category)
    
    def view_expense_vs_income(self):
        """View income vs expenses"""
        income = sum(t.amount for t in self.transactions if t.amount > 0)
        expenses = sum(t.amount for t in self.transactions if t.amount < 0)
        print(f"Income: {income}\nExpenses: {expenses}")
        print(f"Net Balance: {income + expenses}")

    def view_transactions(self):
        """View all transactions"""
        for t in self.transactions:
            print(t)

    def display_menu(self):
        """Display the main menu options."""
        print("\n-- Budget Tracker --")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View All Transactions")
        print("4. View Expense vs Income")
        print("5. Exit")
    
    def get_user_input(self):
        """Prompt for user input to choose an option"""
        try:
            choice = int(input("Choose an option: "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
    
    def handle_add_transaction(self):
        """Handle adding a transaction"""
        try:
            amount = float(input("Enter amount (positive for income, negative for expenses): "))
            category = input(f"Enter category({', '.join(self.categories)}): ")
            description = input("Enter a description: ")
            self.add_transaction(amount, category, description)
        except ValueError:
            print("Invalid input for amount. Please enter a valid number.")

def main():
    """Main function to run the Budget Tracker"""
    budget_tracker = BudgetTracker()

    while True:
        budget_tracker.display_menu()
        choice = budget_tracker.get_user_input()

        if choice == 1:
            budget_tracker.handle_add_transaction()
        elif choice == 2:
            budget_tracker.view_summary()
        elif choice == 3:
            budget_tracker.view_transactions()
        elif choice == 4:
            budget_tracker.view_expense_vs_income()
        elif choice == 5:
            print("Exiting the Budget Tracker.")
            break
        else:
            print("Invalid option, please choose again.")

class Transaction:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.date} | {self.category} | {self.description} | {'+' if self.amount > 0 else '-'}{self.amount}"
    
    def to_dict(self):
        """Convert transaction to dictionary for saving"""
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }

if __name__ == "__main__":
    main()
