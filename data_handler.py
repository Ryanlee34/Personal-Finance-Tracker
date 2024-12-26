import csv
from csv import DictReader

fieldnames= ["Date", "Transaction Type", "Category", "Income Type", "Amount", "Details"]

#Write Data to CSV
def data_processor(functions):
    #Store Results
    results = {}
    #Iterate Through Functions
    for key, func in functions.items():
        results[key] = func()

    with open("transactions.csv", 'a+', newline="") as file:
        #Set pointer to start
        file.seek(0)
        reader = csv.reader(file)
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not any(row for row in reader):
            writer.writeheader()

        writer.writerow(results)




#Print and format CSV Data
def data_output():
    with open("transactions.csv", 'r') as file:
         reader = csv.DictReader(file)
         print(f"{'Date':<20}{'Transaction Type':<30}{'Category':<16}{'Income Type':<21}{'Amount':<12}{'Details':<14}")
         print("-" * 101)
         for row in reader:
            #Adjust Date Format!!
            print(f"{row['Date']:<20}{row['Transaction Type']:<30}{row['Category']:<16}{row['Income Type']:<21}{row['Amount']:<12}{row['Details']:<14}")



#Filter Transactions
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
























