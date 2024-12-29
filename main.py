import sys
import data_handler as data
import Validators as Valid
import visualizations as vis

#Main function to handle user interactions and the menu
def main():

    # Initialize Dictionary linking input fields to their functions
    functions = {
    "Date": Valid.get_valid_date,
    "Transaction Type": Valid.get_transaction_type,
    "Category": Valid.get_category,
    "Income Type": Valid.get_income_type,
    "Amount": Valid.get_amount,
    "Details": Valid.get_description
    }

    #Main menu loop
    while True:
        print("\nMenu Options")
        print("1. -Add Transaction")
        print("2. -View All Transactions")
        print("3. -Filter And View Transactions")
        print("4. -Income or Expense Pie Chart")
        print("5. -Line Chart")
        print("6. -Exit Program")
        user = input("Please Enter the number of Desired option: ")

        #Validate menu input
        if user not in ["1","2","3","4","5","6"]:
            print("Invalid Input, Please Try again")
            continue

        # Option to add new transaction
        if user == "1":
            data.data_processor(functions)
        # Option to view all transactions
        elif user == "2":
            data.data_output()
        # Option to filter and view transactions
        elif user == "3":
            data.data_select()
        # Option to use Pie Chart
        elif user == "4":
            e_or_i = input("1. -Expense Chart \n2. -Income Chart ").strip()
            if e_or_i == "1":
                vis.pie_chart(e_or_i)
            elif e_or_i == "2":
                vis.pie_chart(e_or_i)
            else:
                print("Invalid input. Please try again.")
        # Option to use Line Chart
        elif user == "5":
            vis.line_chart()
        # Exit the program
        elif user == "6":
            sys.exit(0)

        input("\nPress Enter to return to the menu.")


# Entry point for the program execution
if __name__ == "__main__":
    main()
