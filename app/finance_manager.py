from models import Transaction
from database import DatabaseManager
import Validators as Valid

class FinanceManager:
    """
    Manages financial transactions, including adding and retrieving records.
    """

    def __init__(self):
        """Initialize FinanceManager with a DatabaseManager instance."""
        self.db = DatabaseManager()

    def add_transaction(self):
        """
        Gather user input and add a transaction to the database.
        """
        print("\nAdding a new transaction:")
        date = Valid.get_valid_date()
        transaction_type = Valid.get_transaction_type()
        category = Valid.get_category() if transaction_type == "Expense" else None
        income_type = Valid.get_income_type() if transaction_type == "Income" else None
        amount = Valid.get_amount()
        details = Valid.get_description()

        transaction = Transaction(date, transaction_type, category, income_type, amount, details)
        self.db.add_transaction(transaction)
        print("\nTransaction successfully added!")

    def view_transactions(self):
        """Fetch and display all transactions from the database."""
        transactions = self.db.get_all_transactions()  # Fetch fresh data

        if not transactions:
            print("\nNo transactions found.")
            return

        print("\n=== All Transactions ===")
        for txn in transactions:
            print(f"ID: {txn.id} | Date: {txn.date} | Type: {txn.transaction_type} | "
                  f"Category: {txn.category if txn.transaction_type == 'Expense' else txn.income_type} | "
                  f"Amount: ${txn.amount:.2f} | Details: {txn.details}")

    def view_transactions_by_type(self):
        """Retrieve and display transactions filtered by type (Income/Expense)."""
        transaction_type = Valid.get_transaction_type()
        transactions = self.db.get_transactions_by_type(transaction_type)

        if not transactions:
            print(f"\nNo {transaction_type.lower()} transactions found.")
            return

        print(f"\n=== {transaction_type} Transactions ===")
        for txn in transactions:
            print(f"ID: {txn.id} | Date: {txn.date} | Type: {txn.transaction_type} | "
                  f"Category: {txn.category if txn.transaction_type == 'Expense' else txn.income_type} | "
                  f"Amount: ${txn.amount:.2f} | Details: {txn.details}")
