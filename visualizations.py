import matplotlib.pyplot as plt
import pandas as pd
import csv


# Pie chart for expenses by proportion
def pie_chart(typ):
    # Open and read the CSV file
    with open('transactions.csv', 'r') as file:
        reader = csv.DictReader(file)
        data_list = list(reader)  # Convert the reader to a list of dictionaries

    df = pd.DataFrame(data_list)

    # Change amount to float or int
    df['Amount'] = pd.to_numeric(df['Amount'], errors= 'coerce')

    # Select users desired chart
    while True:
        if typ == '1':
            expense_df = df[df['Transaction Type'] == 'Expense']
            plt.title("Expense Distribution by Category")
            grouped = expense_df.groupby('Category')['Amount'].sum()
            break
        else:
            income_df = df[df['Transaction Type'] == 'Income']
            plt.title("Income Distribution by Category")
            grouped = income_df.groupby('Income Type')['Amount'].sum()
            break

    # Create PieChart
    plt.pie(
        grouped,
        labels = grouped.index,
        autopct='%1.1f%%',
        startangle=140,
        shadow=True
    )
    plt.show()


# Line chart for Income vs Expenses over time
def line_chart():
    with open('transactions.csv', 'r') as file:
        reader = csv.DictReader(file)
        data_list = list(reader)  # Convert the reader to a list of dictionaries
        abbreviated_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        df = pd.DataFrame(data_list)
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

        # Change string format to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.month

        # Separate Income and Expense data
        income_group =df[df['Transaction Type'] == 'Income']
        expense_group =df[df['Transaction Type'] == 'Expense']

        # Group by Month and calculate sums
        income_grouped = income_group.groupby('Month')['Amount'].sum()
        expense_grouped =expense_group.groupby('Month')['Amount'].sum()

        # Align months for both groups
        common_months = income_grouped.index.intersection(expense_grouped.index)
        income_grouped = income_grouped.loc[common_months]
        expense_grouped = expense_grouped.loc[common_months]

        #Pepare x (months) and y (values)
        x = common_months
        y1 = income_grouped.values
        y2 = expense_grouped.values

        # Plot Income and Expense data
        plt.plot(x,y1,label = 'Income', marker = 'o')
        plt.plot(x,y2,label = 'Expense', marker = 's')

        # Customize chart
        plt.title("Monthly Income vs Expenses")
        plt.xlabel("Month")
        plt.ylabel("Income vs Expense")
        plt.xticks(ticks=x, labels=[abbreviated_months[i-1] for i in x])
        plt.legend()
        plt.grid(True)

        plt.show()



















