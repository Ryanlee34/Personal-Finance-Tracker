import csv
from csv import DictReader

fieldnames= ["Date", "Transaction Type", "Category", "Income Type", "Amount", "Details"]

# Write transaction data to CSV file
def data_processor(functions):
    # Store Results from user input
    results = {}
    # Iterate Through Functions
    for key, func in functions.items():
        results[key] = func()

    with open("transactions.csv", 'a+', newline="") as file:
        file.seek(0) # Set pointer to start to check for empty file
        reader = csv.reader(file)
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not any(row for row in reader):  # Write header if file is empty
            writer.writeheader()

        writer.writerow(results)    # Append the new transaction




# Reads and prints transaction data from the CSV file in a formatted manner
def data_output():
    with open("transactions.csv", 'r') as file:
         reader = csv.DictReader(file)
         print(f"{'Date':<20}{'Transaction Type':<30}{'Category':<16}{'Income Type':<21}{'Amount':<12}{'Details':<14}")
         print("-" * 101)
         for row in reader:
            #Adjust Date Format!!
            print(f"{row['Date']:<20}{row['Transaction Type']:<30}{row['Category']:<16}{row['Income Type']:<21}{row['Amount']:<12}{row['Details']:<14}")



# Filter Transactions based on user-specified type and category
def data_select():
    try:
        with open("transactions.csv", 'r') as file:
            reader = DictReader(file)
            user = input("Income or Expense?").title().strip()
            user1 = input("Please select a category: Groceries, Bills, Entertainment, Other").title().strip()

            if user not in ["Income", "Expense"]:
                print("Invalid Transaction Type. Please enter 'Income' or 'Expense.'")

            found = False
            for row in reader:
                if row['Transaction Type'] == user and row['Category'] == user1:
                    print(row)
                    found = True

            if not found:
                print("No matching Transactions.")

    except KeyError as e:
        print(f"Key Error: {e}. Please Check CSV headers.")
























