def get_valid_date():
    # Prompts the user for a date and validates its format
    while True:
        user_input = input("Please Enter a date for your Transaction(YYYY-MM-DD): ").strip()
        user_date = user_input.split("-")

        year = user_date[0]
        month = user_date[1]
        day = user_date[2]

        if len(user_date) != 3:
            print("Invalid input")
        elif (
            len(year) != 4 or
            len(month) != 2 or
            len(day) != 2
        ):
            print("Invalid input")

        input_list = [year, month, day]
        converted_list = list(map(int, input_list))

        if not (0000 <= converted_list[0] <= 9999):
            print("Invalid input")
        elif not (1<= converted_list[1] <= 12):
            print("Invalid input")
        elif not (1<= converted_list[2] <= 31):
            print("Invalid input")

        # Format and return the valid date
        str_list = list(map(str, converted_list))
        final_date = "-".join(str_list)
        return final_date

# Prompts the user to specify if the transaction is income or expense
def get_transaction_type():
    while True:
        user_type = input("Will this be an income or expense? ").title().strip()
        if user_type == "Income":
            return "Income"
        elif user_type == "Expense":
            return "Expense"
        else:
            print("Invalid input, please enter income or expense!")
            continue


# Prompts the user to select a category for expense transactions
def get_category():
    while True:
        user_category = input("Please select a Category from the Following: Groceries, Bills, Entertainment, Other ").title().strip()
        if user_category == "Groceries":
            return "Groceries"
        elif user_category == "Bills":
            return "Bills"
        elif user_category == "Entertainment":
            return "Entertainment"
        elif user_category == "Other":
            return "Other"
        print("Invalid Category")


# Prompts the user to specify the origin of income transactions
def get_income_type():
    while True:
            user_income = input("Please Select the origin of the income: Paycheck, Refund, Dividends, Other ").title().strip()
            if user_income == "Paycheck":
                return "Paycheck"
            elif user_income == "Refund":
                return "Refund"
            elif user_income == "Dividends":
                return "Dividends"
            elif user_income == "Other":
                return "Other"
            print("Invalid Category")

# Validates and converts the amount to a float
def get_amount():
    while True:
        user_amount = input("Please enter in the amount for this transaction(00.00):").strip()
        try:
            user_dollar_amount = float(user_amount)
            return user_dollar_amount
        except ValueError:
            print("Invalid input, try again")

# Captures and returns a description for the transaction
def get_description():
    user_description = input("Enter a Description of Purchase: ").title()
    return user_description