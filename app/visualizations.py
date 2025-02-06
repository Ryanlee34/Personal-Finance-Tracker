import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
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

def pie_chart(transaction_type):
    """Generate a pie chart for income/expense distribution."""
    engine = get_database_engine()
    if not engine:
        print("Cannot generate chart. Database connection failed.")
        return

    # Determine the correct column to group by
    column_name = "category" if transaction_type == "Expense" else "income_type"

    query = f"""
        SELECT {column_name} AS label, SUM(amount) as total 
        FROM transactions 
        WHERE transaction_type = %(transaction_type)s
        GROUP BY {column_name}
    """

    with engine.connect() as connection:
        df = pd.read_sql_query(query, connection, params={"transaction_type": transaction_type})

    if df.empty:
        print(f"No {transaction_type.lower()} data available.")
        return

    # Debugging: Print retrieved data
    print("\nDEBUG: Data Retrieved for Pie Chart")
    print(df)

    plt.figure(figsize=(8, 6))
    plt.pie(df['total'], labels=df['label'], autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title(f"{transaction_type} Distribution by {'Category' if transaction_type == 'Expense' else 'Income Type'}")
    plt.show()

def line_chart():
    """Generate a line chart of income vs. expenses over time."""
    engine = get_database_engine()
    if not engine:
        print("Cannot generate chart. Database connection failed.")
        return

    query = """
        SELECT date, transaction_type, SUM(amount) as total 
        FROM transactions 
        GROUP BY date, transaction_type 
        ORDER BY date
    """

    with engine.connect() as connection:
        df = pd.read_sql_query(query, connection)

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



