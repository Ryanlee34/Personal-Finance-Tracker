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


    # Open the CSV file in append mode, ensuring data is preserved
    with open("transactions.csv", 'a+', newline="") as file:
        file.seek(0) # Set pointer to start to check for empty file
        reader = csv.reader(file)
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header only if the file is empty
        if not any(row for row in reader):
            writer.writeheader()

        # Write the new transaction data as a row in the file
        writer.writerow(results)    #




# Function to read and print transaction data from the CSV file in a formatted way
def data_output():
    with open("transactions.csv", 'r') as file:
         reader = csv.DictReader(file)
         # Print table headers with appropriate spacing
         print(f"{'Date':<20}{'Transaction Type':<30}{'Category':<16}{'Income Type':<21}{'Amount':<12}{'Details':<14}")
         print("-" * 101) # Separator line for readability
         for row in reader:
            # Print each row of data, aligning columns for consistent output
            print(f"{row['Date']:<20}{row['Transaction Type']:<30}{row['Category']:<16}{row['Income Type']:<21}{row['Amount']:<12}{row['Details']:<14}")



# Function to filter transactions based on user-specified type and category
def data_select():
    try:
        # Open the CSV file for reading
        with open("transactions.csv", 'r') as file:
            reader = DictReader(file)
            # Prompt the user for transaction type and category filters
            user = input("Income or Expense?").title().strip()
            user1 = input("Please select a category: Groceries, Bills, Entertainment, Other").title().strip()

            # Validate user input for transaction type
            if user not in ["Income", "Expense"]:
                print("Invalid Transaction Type. Please enter 'Income' or 'Expense.'")

            found = False # Flag to track if matching transactions are found
            # Iterate through the rows to find matches based on user input
            for row in reader:
                if row['Transaction Type'] == user and row['Category'] == user1:
                    print(row)
                    found = True

            # Notify the user if no matching transactions are found
            if not found:
                print("No matching Transactions.")

    except KeyError as e:
        # Handle cases where the CSV headers are incorrect or missing
        print(f"Key Error: {e}. Please Check CSV headers.")
























