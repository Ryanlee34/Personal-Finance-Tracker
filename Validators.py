def get_valid_date():
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
            #Need to alter later to include exceptions on 30 day months
        elif not (1<= converted_list[2] <= 31):
            print("Invalid input")

        #Finish Reconversion and Formatting here!
        final_list = list(map(int, converted_list))
        return final_list


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


# only use this function if user selects expense
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


# Income selection only
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


def get_amount():
    while True:
        user_amount = input("Please enter in the amount for this transaction(00.00):").strip()
        try:
            user_dollar_amount = float(user_amount)
            return user_dollar_amount
        except ValueError:
            print("Invalid input, try again")


def get_description():
    user_description = input("Enter a Description of Purchase: ").title()
    return user_description