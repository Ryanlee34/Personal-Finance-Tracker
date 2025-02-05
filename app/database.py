import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class DatabaseManager:
    """
    Handles database interactions for storing and retrieving transactions.
    """

    def __init__(self):
        """Initialize the database connection using credentials from .env."""
        try:
            self.conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
            self.cursor = self.conn.cursor()
            print("Database connection successful.")
        except psycopg2.OperationalError as e:
            print("Database connection error. Check your credentials.")
            print(e)
            self.conn = None

    def add_transaction(self, transaction):
        """
        Insert a new transaction into the database.

        Args:
            transaction (Transaction): The transaction object to be stored.
        """
        if not self.conn:
            print("Cannot add transaction. Database is not connected.")
            return

        query = """
        INSERT INTO transactions (date, transaction_type, category, income_type, amount, details)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (transaction.date, transaction.transaction_type, transaction.category,
                  transaction.income_type, transaction.amount, transaction.details)

        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute(query, values)
            print("Transaction added successfully.")
        except psycopg2.Error as e:
            print("Error inserting transaction:", e)

    def get_all_transactions(self):
        """
        Retrieve all transactions from the database.

        Returns:
            list: A list of transactions.
        """
        if not self.conn:
            print("Cannot retrieve transactions. Database is not connected.")
            return []

        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
                    transactions = cursor.fetchall()
            return transactions
        except psycopg2.Error as e:
            print("Error retrieving transactions:", e)
            return []

    def get_transactions_by_type(self, transaction_type):
        """
        Retrieve transactions of a specific type (Income/Expense).

        Args:
            transaction_type (str): The type of transaction to filter by.

        Returns:
            list: A list of filtered transactions.
        """
        if not self.conn:
            print("Cannot retrieve transactions. Database is not connected.")
            return []

        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM transactions WHERE transaction_type = %s ORDER BY date DESC",
                        (transaction_type,)
                    )
                    transactions = cursor.fetchall()
            return transactions
        except psycopg2.Error as e:
            print("Error retrieving filtered transactions:", e)
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self

