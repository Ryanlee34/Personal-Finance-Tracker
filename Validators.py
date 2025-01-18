# Function to validate and return a user-entered date in the format YYYY-MM-DD
def get_valid_date():
    # Prompts the user for a date and validates its format
    while True:
        user_input = input("Please Enter a date for your Transaction(YYYY-MM-DD): ").strip()
        user_date = user_input.split("-")

        # Extract year, month, and day from the user input
        year = user_date[0]
        month = user_date[1]
        day = user_date[2]

        # Ensure the input has three components (year, month, day)
        if len(user_date) != 3:
            print("Invalid input")
        elif (
            len(year) != 4 or
            len(month) != 2 or
            len(day) != 2
        ):
            print("Invalid input")

        # Convert input components into integers for validation
        input_list = [year, month, day]
        converted_list = list(map(int, input_list))

        # Validate the year, month, and day ranges
        if not (0000 <= converted_list[0] <= 9999):
            print("Invalid input")
        elif not (1<= converted_list[1] <= 12):
            print("Invalid input")
        elif not (1<= converted_list[2] <= 31):
            print("Invalid input")
        # Handle months with only 30 days
        elif converted_list[1] in [4,6,9,11] and converted_list[2] > 30: # Handle months with 30 days
            print("Invalid input, this month only had 30 days")
        # Handle February, including leap year logic
        elif converted_list[1] == 2:
            if (converted_list[0] % 4 == 0 and converted_list[0] % 100 != 0) or (converted_list[0] % 400 == 0): # Leap year check
                if converted_list[2] > 29:
                    print("Invalid input, February has at most 29 days in a leap year")
            elif converted_list[2] > 28: # Handle February
                print("Invalid input, February has at most 28 days")
        else:
            # Format and return the valid date
            str_list = list(map(str, converted_list))
            final_date = "-".join(str_list)
            return final_date

# Function to prompt the user to specify if the transaction is income or expense
def get_transaction_type():
    while True:
        # Prompt the user for the transaction type
        user_type = input("Will this be an income or expense? ").title().strip()
        # Validate the input
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
        # Provide predefined categories for selection
        user_category = input("Please select a Category from the Following: Groceries, Bills, Entertainment, Other ").title().strip()
        # Validate the category and return it
        if user_category == "Groceries":
            return "Groceries"
        elif user_category == "Bills":
            return "Bills"
        elif user_category == "Entertainment":
            return "Entertainment"
        elif user_category == "Other":
            return "Other"
        print("Invalid Category")


# Function to prompt the user to specify the origin of income transactions
def get_income_type():
    while True:
            # Provide predefined income types for selection
            user_income = input("Please Select the origin of the income: Paycheck, Refund, Dividends, Other ").title().strip()
            # Validate the income type and return it
            if user_income == "Paycheck":
                return "Paycheck"
            elif user_income == "Refund":
                return "Refund"
            elif user_income == "Dividends":
                return "Dividends"
            elif user_income == "Other":
                return "Other"
            print("Invalid Category")

# Function to validate and convert the amount to a float
def get_amount():
    while True:
        user_amount = input("Please enter in the amount for this transaction(00.00):").strip()
        try:
            # Convert the input to a float and return it
            user_dollar_amount = float(user_amount)
            return user_dollar_amount
        except ValueError:
            print("Invalid input, try again")

# Function to capture and return a description for the transaction
def get_description():
    # Prompt the user to enter a description of the transaction
    user_description = input("Enter a Description of Purchase: ").title()
    return user_description