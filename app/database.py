from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_database_engine():
    """Create a SQLAlchemy engine for database connection."""
    db_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    try:
        engine = create_engine(db_url)
        return engine
    except Exception as e:
        print("Error creating database engine:", e)
        return None

class DatabaseManager:
    """Handles database interactions for storing and retrieving transactions."""

    def __init__(self):
        """Initialize the database connection."""
        self.engine = get_database_engine()
        if self.engine:
            print("Database connection successful.")

    def add_transaction(self, transaction):
        """Insert a new transaction into the database."""
        if not self.engine:
            print("Cannot add transaction. Database is not connected.")
            return

        query = text("""
            INSERT INTO transactions (date, transaction_type, category, income_type, amount, details)
            VALUES (:date, :transaction_type, :category, :income_type, :amount, :details)
        """)

        values = {
            "date": transaction.date,
            "transaction_type": transaction.transaction_type,
            "category": transaction.category if transaction.transaction_type == "Expense" else None,
            "income_type": transaction.income_type if transaction.transaction_type == "Income" else None,
            "amount": transaction.amount,
            "details": transaction.details
        }

        with self.engine.begin() as connection:
            try:
                connection.execute(query, values)
                print("Transaction added successfully.")
            except Exception as e:
                print("Error inserting transaction:", e)

    def get_all_transactions(self):
        """Retrieve all transactions from the database."""
        if not self.engine:
            print("Cannot retrieve transactions. Database is not connected.")
            return []

        query = text("SELECT id, date, transaction_type, category, income_type, amount, details FROM transactions ORDER BY date DESC")

        with self.engine.connect() as connection:
            result = connection.execute(query)
            transactions = result.fetchall()

        if not transactions:
            print("\nNo transactions found.")
            return []

        return transactions

    def get_transactions_by_type(self, transaction_type):
        """Retrieve transactions filtered by type (Income/Expense)."""
        if not self.engine:
            print("Cannot retrieve transactions. Database is not connected.")
            return []

        query = text("""
            SELECT id, date, transaction_type, category, income_type, amount, details 
            FROM transactions 
            WHERE transaction_type = :transaction_type 
            ORDER BY date DESC
        """)

        with self.engine.connect() as connection:
            result = connection.execute(query, {"transaction_type": transaction_type})
            transactions = result.fetchall()

        if not transactions:
            print(f"\nNo {transaction_type.lower()} transactions found.")
            return []

        return transactions

