from datetime import datetime

def get_valid_date():
    """Prompt user for a valid transaction date (YYYY-MM-DD)."""
    while True:
        user_input = input("Enter transaction date (YYYY-MM-DD): ").strip()
        try:
            valid_date = datetime.strptime(user_input, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_transaction_type():
    """Prompt user to enter 'Income' or 'Expense'."""
    while True:
        user_type = input("Is this an Income or Expense? ").title().strip()
        if user_type in ["Income", "Expense"]:
            return user_type
        print("Invalid input! Enter 'Income' or 'Expense'.")

def get_category():
    """Prompt user to select a predefined category for expenses."""
    categories = ["Groceries", "Bills", "Entertainment", "Other"]
    while True:
        category = input(f"Choose a category {categories}: ").title().strip()
        if category in categories:
            return category
        print("Invalid category, try again.")

def get_income_type():
    """Prompt user to select an income source, if applicable."""
    income_types = ["Paycheck", "Refund", "Dividends", "Other"]
    while True:
        income_type = input(f"Choose an income source {income_types}: ").title().strip()
        if income_type in income_types:
            return income_type
        print("Invalid income type, try again.")

def get_amount():
    """Prompt the user to enter a valid transaction amount (positive number)."""
    while True:
        try:
            amount = float(input("Enter the transaction amount: ").strip())
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")

def get_description():
    """Prompt user to enter a short description for the transaction."""
    while True:
        description = input("Enter a short description for the transaction: ").strip()
        if len(description) > 0:
            return description
        print("Description cannot be empty.")
