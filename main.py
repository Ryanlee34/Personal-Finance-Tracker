import sys
import data_handler as data
import Validators as Valid


def main():

    # Initialize Dictionary
    functions = {
    "Date": Valid.get_valid_date,
    "Transaction Type": Valid.get_transaction_type,
    "Category": Valid.get_category,
    "Income Type": Valid.get_income_type,
    "Amount": Valid.get_amount,
    "Details": Valid.get_description
    }

    #Create menu
    while True:
        print("Menu Options")
        print("1. -Add Transaction")
        print("2. -View All Transactions")
        print("3. -Filter And View Transactions")
        print("4. -Exit Program")
        user = input("Please Enter the number of Desired option: ")

        if user not in ["1","2","3","4"]:
            print("Invalid Input, Please Try again")
            continue


        if user == "1":
            data.data_processor(functions)
        elif user == "2":
            data.data_output()
        elif user == "3":
            data.data_select()
        elif user == "4":
            sys.exit(0)


if __name__ == "__main__":
    main()
