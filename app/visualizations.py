import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_database_connection():
    """Connect to the database and return a connection object."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def pie_chart(transaction_type):
    """Generate a pie chart for income/expense distribution."""
    conn = get_database_connection()
    df = pd.read_sql(f"SELECT category, SUM(amount) as total FROM transactions WHERE transaction_type='{transaction_type}' GROUP BY category", conn)
    conn.close()

    if df.empty:
        print(f"No {transaction_type.lower()} data available.")
        return

    plt.figure(figsize=(8, 6))
    plt.pie(df['total'], labels=df['category'], autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title(f"{transaction_type} Distribution by Category")
    plt.show()

def line_chart():
    """Generate a line chart of income vs expenses over time."""
    conn = get_database_connection()
    df = pd.read_sql("""
        SELECT date, transaction_type, SUM(amount) as total 
        FROM transactions 
        GROUP BY date, transaction_type 
        ORDER BY date
    """, conn)
    conn.close()

    if df.empty:
        print("No transaction data available.")
        return

    income_df = df[df['transaction_type'] == 'Income']
    expense_df = df[df['transaction_type'] == 'Expense']

    plt.figure(figsize=(10, 5))
    plt.plot(income_df['date'], income_df['total'], marker='o', label='Income')
    plt.plot(expense_df['date'], expense_df['total'], marker='s', label='Expense')
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income vs Expenses Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()













